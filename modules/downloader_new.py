

import shlex
from time import sleep
from pathlib import Path
from zipfile import ZipFile
# from traceback import format_exc, print_exc
from argparse import ArgumentParser
from platform import processor
from sys import exit, platform, version_info
from subprocess import Popen, run, PIPE, DEVNULL

try:
    from requests import Session
    from psutil import process_iter, NoSuchProcess, AccessDenied, ZombieProcess
    import undetected_chromedriver as uc
    from selenium import webdriver
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from selenium.webdriver import ActionChains #, Keys
    # from selenium.common.exceptions import ElementNotVisibleException
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
except (ImportError, ModuleNotFoundError):
    print("\nModules are not installed!")
    exit("Run 'pip install requirements.txt' in the terminal to fix errors.")


if platform not in ("darwin", "linux", "win32"):
    exit("OS configurations not available yet.")


parser = ArgumentParser(
    prog="Predespacho Daemon",
    description="Fetches files form the CND server.",
    epilog="Let's demonize CNDz."
)

parser.add_argument("-p", "--port", type=int, default=9001)
parser.add_argument("-b", "--binary", type=str, default="default")
parser.add_argument("-m", "--mode", type=str, default="debug")
args = parser.parse_args()

if args.binary not in ("default", "undetected"):
    exit(f"Invalid binary '{args.binary}'.")

if args.mode not in ("debug", "release"):
    exit(f"Invalid mode '{args.mode}'.")

# Sort shell arguments for subprocesses
shell_arg = True if platform == "win32" else False


def clear() -> int:
    return run(args=["cls" if platform == "win32" else "clear"], shell=shell_arg)


def win32_analyser(command: str) -> str:
    """
    Returns a valid subprocess runner command for Windows.
    """
    return 'powershell -command ' + '"&{' + command + '}"'


def downloader(destination_path: Path | str, download_url: str, custom_file_name: str = None, verify_cert: bool = True) -> bool:
    """
    Downloads whatever with curl.
    - destination_path: Path to store downloaded file.
    - download_url: File download url.
    - custom_file_name: Custom file name for downloaded file.
    """
    # -k/--insecure
    # --cacert [file]
    temp_destination_path = f"'{destination_path}'" if platform == "win32" else destination_path

    if custom_file_name:
        # download_command = f"curl {'--insecure' if not verify_cert else ''} --output {custom_file_name} --create-dirs -O --output-dir {temp_destination_path} {download_url}"
        download_command = f"curl {'--insecure' if not verify_cert else ''} --output {custom_file_name} --output-dir {temp_destination_path} {download_url}"

        # Essential for renaming of failed downloads
        move_command = f"mv {destination_path.joinpath(custom_file_name)} {destination_path.joinpath(f'{custom_file_name}.failed')}"

    else:
        # download_command = f"curl {'--insecure' if not verify_cert else ''} --create-dirs -O --output-dir {temp_destination_path} {download_url}"
        download_command = f"curl {'--insecure' if not verify_cert else ''} -O --output-dir {temp_destination_path} {download_url}"

        # Essential for renaming of failed downloads
        file_name = download_url.split('/')[-1]
        move_command = f"mv {destination_path.joinpath(file_name)} {destination_path.joinpath(f'{file_name}.failed')}"

    # Launch the curler and get the job done
    try:
        with Popen(args=shlex.split(download_command), stderr=DEVNULL, shell=shell_arg) as curler:

            is_done = curler.poll()
            while is_done is None:
                sleep(1)
                is_done = curler.poll()
                
            return True
    except:
        # Rename failed downloads by appending a '.failed' suffix to their names
        if platform == "win32": move_command = win32_analyser(command=move_command)

        run(args=shlex.split(move_command), stderr=DEVNULL, shell=shell_arg)
        return False
    finally:
        curler.terminate()
        curler.wait()


def get_browser_version() -> bool | str:
    """
    Fetches version of currently installed Google Chrome browser.
    """
    # Get browser version
    match platform:

        # For Windows
        case "win32":

            # Powershell
            # Older versions install to the 32-bit directory
            # (Get-Item 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe').VersionInfo.ProductVersion

            # Newer versions use the 64-bit directory
            # (Get-Item 'C:\Program Files\Google\Chrome\Application\chrome.exe').VersionInfo.ProductVersion

            # To using it in cmd.exe or via any subprocess calls (python, go os/exec, etc.) you can do,
            # powershell -command "&{(Get-Item 'Path\To\chrome.exe').VersionInfo.ProductVersion}"

            browser_path = Path("C:\\").joinpath("Program Files").joinpath("Google").joinpath("Chrome").joinpath("Application").joinpath("chrome.exe")
            version_command = f"(Get-Item '{browser_path}').VersionInfo.ProductVersion"
            version_command = win32_analyser(command=version_command)

        # For macOS
        case "darwin":

            # Full browser path
            # version_command = "/Applications/'Google Chrome.app'/Contents/MacOS/'Google Chrome' --version"

            browser_path = Path("/Applications").joinpath("Google Chrome.app").joinpath("Contents").joinpath("MacOS").joinpath("Google Chrome")
            version_command = f"'{browser_path}' --version"

        # For Linux
        case "linux":
            version_command = "google-chrome --version"
    
    try:
        with Popen(args=shlex.split(version_command), stdout=PIPE, stderr=DEVNULL, shell=shell_arg) as curler:
            output = curler.stdout.read().strip().decode()
            browser_version = output.split(" ")[-1].split(".")[0]
            
    except:
        return False
    finally:
        curler.terminate()
        curler.wait()

    return browser_version


def fetch_chromedriver() -> bool | str:
    """
    Downloads the latest chromedriver binary from Google servers.
    """
    browser_version = get_browser_version()
    if not browser_version:
        return False
    
    with Session() as driver_session:

        response = driver_session.get(url="https://googlechromelabs.github.io/chrome-for-testing/known-good-versions-with-downloads.json")
        if response.status_code != 200:
            return False
        
        found = False
        all_versions: list = response.json()["versions"]
        for version in all_versions:
            if version["version"].split(".")[0] == browser_version:
                response_data: list = version["downloads"]["chromedriver"]
                found = True
                break

        if not found:
            return False

    # For platform specific chromedriver download
    match platform:
        case "darwin":
            selected_platform = "mac-arm64" if processor() == "arm" else "mac-x64"
        case "linux" | "linux2":
            selected_platform = "linux64"
        case "win32":
            selected_platform = "win32"
        case "win64":
            selected_platform = "win64"

    # Download binary for selected platform
    for data in response_data:
        if data["platform"] == selected_platform:
            download_url = data["url"]

            print("Fetching debug driver, please wait...")
            is_downloaded = downloader(destination_path=core_data_path, download_url=download_url)
            if not is_downloaded:
                return False
            
            return download_url.split("/")[-1]
            
    return False


def process_binary(fetched_file: str) -> bool:
    """
    Processes the newly downloaded chromedriver binary for usage.
    """
    zipped_binary = core_data_path.joinpath(fetched_file)
    extracted_binary_folder = core_data_path.joinpath(fetched_file.replace('.zip', ''))
    extracted_binary = extracted_binary_folder.joinpath('chromedriver.exe' if platform == 'win32' else 'chromedriver')

    try:
        print("Processing binary...")
        # Delete the existing binary
        if binary_executable_path.is_file():
            binary_executable_path.unlink()
            sleep(1)

        # Unzip the zipped binary
        if zipped_binary.is_file():
            with ZipFile(file=zipped_binary, mode="r") as file:
                file.extractall(path=core_data_path)
            sleep(1)

        # Move the extracted binary to the core_data_folder
        if extracted_binary.is_file():
            extracted_binary.replace(target=binary_executable_path)
            sleep(1)

        # Delete the extracted binary folder
        if extracted_binary_folder.is_dir():
            remove_command = f"rm -r {extracted_binary_folder}"
            if platform == "win32": remove_command = win32_analyser(command=remove_command)
            
            run(args=shlex.split(remove_command), stderr=DEVNULL)
            sleep(1)

        # Delete the zipped binary
        if zipped_binary.is_file():
            zipped_binary.unlink()
            sleep(1)

        # Fix permissions for extracted binary on macOS and Linux
        if platform != "win32" and binary_executable_path.is_file():
            fix_command = f"chmod 755 {binary_executable_path}"

            run(args=shlex.split(fix_command), stderr=DEVNULL)
            sleep(1)

        return True
    except:
        return False


def compose_launch_command(headless: bool, data_directory: str, port: int | None = None) -> str:
    """
    Composes a command to launch browsers on different OS
    """
    match platform:

        # For Windows
        case "win32":
            browser_launch_path = Path('C:\\').joinpath('Program Files').joinpath('Google').joinpath('Chrome').joinpath('Application').joinpath('chrome.exe')
            browser_launch_path = f"'{browser_launch_path}'"

        # For macOS
        case "darwin":
            browser_launch_path = Path("/Applications").joinpath("Google Chrome.app").joinpath("Contents").joinpath("MacOS").joinpath("Google Chrome")
            browser_launch_path = f"'{browser_launch_path}'"


        # For Linux
        case "linux":
            browser_launch_path = "google-chrome"
    
    final_command = f"{browser_launch_path} {f'--remote-debugging-port={port}' if port else ''} --user-data-dir='{data_directory}' {'--headless=new' if headless else ''} --no-first-run --start-maximized"
    return final_command


def wait_for_chrome() -> None:
    """
    Waits for Google Chrome to launch efficiently.
    """
    checked_processes = 0
    while checked_processes < 7:

        # Possible race condition due to permissions error on macOS.
        # Explained at: https://github.com/giampaolo/psutil/issues/2189
        
        # # First fix method
        # for process in process_iter(attrs=["name"]):
        #     if "chrome" in process.info["name"].lower(): checked_processes += 1

        # Second fix method
        for process in process_iter():
            try:
                if "chrome" in process.name().lower(): checked_processes += 1
            except (NoSuchProcess, AccessDenied, ZombieProcess):
                continue

        sleep(2)

    sleep(3)


def initialize_chrome_session(headless: bool = True) -> bool | Popen:
    """
    Starts up Google Chrome from a dedicated profile directory.
    If an active directory is unavailable, it is created.
    - headless: Flag indicates if browser would be seen or not.
    """
    is_new = False

    # Check for persistent chrome folder
    if not chromecache_path.is_dir():
        is_new = True
        print("Crafting new chrome profile. Please wait...")
    else:
        print("Spooling up...")

    launch_command = compose_launch_command(headless=headless, port=args.port, data_directory=chromecache_path)    
    try:
        new_chrome = Popen(args=shlex.split(launch_command), stderr=DEVNULL)
        wait_for_chrome()

        if is_new:
            print("Done crafting profile.")

        return new_chrome
    except:
        print("An error occured!")
        new_chrome.terminate()
        new_chrome.wait()
        return False
    finally:
        sleep(1)


def clean_up():
    """
    Removes old failed downloads and backs up completed downloads.
    """
    for file in temp_folder_path.iterdir():
        if file.suffix not in (".xlsx", ".xls"):
            file.unlink()
        else:
            file.rename(target=backup_folder_path.joinpath(file.name))


class Automate:

    def __init__(self, 
                 debug: bool = False, 
                 headless: bool = True, 
                 undetected: bool = False, 
                 slave: bool = False, 
                 port: int = 9000, 
                 browser_version: int = 108, 
                 load_images: bool = True, 
                 ) -> None:
        
        # Guide
        """
        Defaults:
        - debug: Uses embedded driver binary if set to True.
        - headless: Sets headless property.
        - undetected: Runs headless Chrome browser with undetected-chromedriver. Compatible with only Python 3.11.*.
        - slave: Toggles slave mode (takes over already open browser window if set to True).
        - port: Port used by Chrome browser to connect to in slave mode.
        - browser_version: Rounded up Chrome browser version.
        - load_images: Sets image load property.
        """
        
        # Default constructor flags
        self.debug = debug
        self.headless = headless
        self.undetected = undetected
        self.slave = slave
        self.port = port
        self.browser_version = browser_version
        self.load_images = load_images

        # Check for chromedriver and/or undetected_chromedriver
        if self.debug and not binary_executable_path.is_file():
            print("Error! chromedriver was not found.")
            raise SystemExit

        if self.slave and not self.port:
            print("Error! You must declare an open port.")
            raise SystemExit

        # Custom flag management
        self.webdriver = webdriver
    
        if self.undetected:
            self.webdriver = uc
            
            # Checks for Python version (3.8.* - 3.11.*)
            if version_info.major != 3 or version_info.minor not in (8, 9, 10, 11):
                print("Error! Invalid Python version. Undetected mode is only compatible with Python 3.8 - 3.11")
                raise SystemExit

        if self.slave: self.headless = True

        self.Options = Options
        self.Service = Service


    def core(self) -> tuple:
        """
        Prepares core session configurations.
        """
        options = self.Options()
        options.add_argument("--start-maximized") # Maximize browser window to fix view ports

        # Headless mode argument
        if self.headless: options.add_argument("--headless=new")

        # Manages image loads
        if not self.load_images: options.add_argument("--blink-settings=imagesEnabled=false")

        # Slave mode management
        if self.slave: options.add_argument(f"--remote-debugging-port={self.port}")

        service = self.Service(executable_path=binary_executable_path) if self.debug else self.Service()
        # service = self.Service(executable_path=undetected_binary_executable_path) if self.debug else self.Service()

        # ===== DISABLE WebRTC features =====
        options.add_argument("--enforce-webrtc-ip-permission-check")
        options.add_argument("--webrtc-ip-handling-policy=disable_non_proxied_udp")
        options.add_argument("--force-webrtc-ip-handling-policy")
        options.add_argument('--use-fake-ui-for-media-stream')
        options.add_argument('--use-fake-device-for-media-stream')
        options.add_argument("--disable-media-session-api")

        # ===== CHROMIUM BASED ANONYMITY FEATURES =====
        if self.undetected:
            options.add_argument('--disable-gpu')
        else:
            options.add_argument("--disable-blink-features=AutomationControlled") # Adding argument to disable the AutomationControlled flag
            options.add_experimental_option("excludeSwitches", ["enable-automation"]) # Exclude the collection of enable-automation switches
            options.add_experimental_option("useAutomationExtension", False) # Turn-off userAutomationExtension

        return options, service


    def session(self):
        """
        Fires up the session.
        """
        try:
            clear()
            print("Spawning session...")
            options, service = self.core()

            BrowserClass = self.webdriver.Chrome

            if self.webdriver.__name__ == "selenium.webdriver":
                driver = BrowserClass(options=options, service=service)
            elif self.webdriver.__name__ == "undetected_chromedriver":
                driver = BrowserClass(options=options, driver_executable_path=str(binary_executable_path) if platform == "win32" else binary_executable_path, port=self.port, version_main=self.browser_version) if self.debug else BrowserClass(options=options, port=self.port, version_main=self.browser_version)

            wait = WebDriverWait(driver=driver, timeout=30)
            action = ActionChains(driver=driver)

            # ===== GENERAL ANONYMITY FEATURES =====
            if not self.slave:
                # Changing the property of the navigator value for webdriver to undefined
                driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

            # Fix headless UAs
            user_agent = driver.execute_script('return navigator.userAgent;')
            for i in ("Headless", "headless"):
                if i in user_agent:
                    user_agent = user_agent.replace(i, "")

                    # Spoof User-Agent on the fly for chromium based browsers
                    driver.execute_cdp_cmd("Network.setUserAgentOverride", {"userAgent": user_agent})
                    # driver.execute_cdp_cmd("Emulation.setUserAgentOverride", {"userAgent": user_agent})
                    break

            return driver, wait, action
        except KeyboardInterrupt:
            print("\nInterrupted by user.")


def handler(file_name: str, file_url: str) -> None:
    """
    Downloads new predespacho documents.
    """
    try:
        driver.get(file_url)
        wait.until(EC.title_is("Listado website"))
        wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="t-fht-wrapper"]'))) # Table wrapper
        wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@id="stickyTableHeader_1"]'))) # Table head
        wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="t-fht-tbody"]'))) # Table body

        all_table_rows = driver.find_element(By.XPATH, '//div[@class="t-fht-tbody"]').find_element(By.TAG_NAME, "tbody").find_elements(By.TAG_NAME, "tr")
        
        if len(all_table_rows) < 2:
              return

        top_most_row = all_table_rows[1]

        document_data = top_most_row.find_elements(By.TAG_NAME, "td")
        document_name = document_data[0].text.strip()
        formatted_name = document_name.replace("/", "").replace(" ", "_") + ".xlsx"
        document_download_url = document_data[1].find_element(By.TAG_NAME, "a").get_attribute("href")

        print(f"\nDownloading {formatted_name}, please wait...")
        is_downloaded = downloader(destination_path=temp_folder_path, download_url=document_download_url, custom_file_name=formatted_name)
        if not is_downloaded:
            print(f"{file_name} failed to download.")
        else:
            print(f"{formatted_name} successfully downloaded.")
    except:
        print(f"\n{file_name} failed to download.")


def generate_puppies(debug_mode: bool = True, port: int = args.port, load_images: bool = True, retrying: bool = False):
    """
    Generates an active instance of webdriver, WebDriverWait and ActionChains.
    """
    # Defaults to debug mode
    try:
        driver, wait, action = Automate(debug=debug_mode, undetected=True, slave=True, port=port, load_images=load_images, browser_version=int(get_browser_version())).session()
        return driver, wait, action
    except KeyboardInterrupt:
        print("\nInterrupted by user!")
    except:
        if debug_mode:
            
            if retrying:
                # Launch in release mode
                print("Debug mode error! Falling back to Release mode...")
                sleep(3)
                print("Fetching release driver, please wait...")
                return generate_puppies(debug_mode=False, port=port, load_images=load_images)

            is_fetched = fetch_chromedriver()
            if not is_fetched:
                print("Couldn't fetch latest binary!")
                raise SystemExit

            is_processed = process_binary(fetched_file=is_fetched)
            if not is_processed:
                print("Couldn't process binary!")
                raise SystemExit
            
            # Retry launching in debug mode with latest driver
            return generate_puppies(retrying=True, port=port, load_images=load_images)

        # A higher level error due to failure of release mode
        print("Critical Error! Please contact your administrator.")
        raise SystemExit



if __name__ == "__main__":

    clear()
    # Core paths
    runtime_path: Path = Path(__file__).parent
    parent_runtime_path = runtime_path.parent
    desktop_path: Path = Path("~/Desktop").expanduser()

    # Data files
    core_data_path = parent_runtime_path.joinpath("core_data")
    backup_folder_path = core_data_path.joinpath("backup")
    temp_folder_path = core_data_path.joinpath("temp")
    chromecache_path = core_data_path.joinpath("chromecache")

    # Unify chrome binaries
    match args.binary:
        case "default":
            binary_executable_path = core_data_path.joinpath("chromedriver.exe" if platform == "win32" else "chromedriver")
        case "undetected":
            binary_executable_path = core_data_path.joinpath("undetected_chromedriver.exe" if platform == "win32" else "undetected_chromedriver")

    # Sort runtime modes
    is_debug = True if args.mode == "debug" else False

    # Check for core_data folder
    if not core_data_path.is_dir():
        core_data_path.mkdir(parents=True, exist_ok=True)

    # Check for backup folder
    if not backup_folder_path.is_dir():
        backup_folder_path.mkdir(parents=True, exist_ok=True)

    # Check for temp folder
    if not temp_folder_path.is_dir():
        temp_folder_path.mkdir(parents=True, exist_ok=True)

    urlF = {
        # "url" : "https://otr.ods.org.hn:3200/odsprd/f?p=110:4:::::p4_id:4",
        "url" : "https://appcnd.enee.hn:3200/odsprd/f?p=110:4:::::p4_id:4",
        "name" : "Predespacho Final",
    }

    urlS = {
        # "url" : "https://otr.ods.org.hn:3200/odsprd/f?p=110:4:::::p4_id:5",
        "url" : "https://appcnd.enee.hn:3200/odsprd/f?p=110:4:::::p4_id:5",
        "name" : "Predespacho Semanal",
    }

    # Launch the browser and get the job done
    new_chrome = initialize_chrome_session(headless=False)
    if not new_chrome:
        exit()

    try:
        driver, wait, action = generate_puppies(debug_mode=is_debug, load_images=False)
    except:
        new_chrome.terminate()
        new_chrome.wait()
        exit()

    try:
        clean_up()
        for provider in (urlF, urlS):

            try:
                handler(file_name=provider["name"], file_url=provider["url"])
            except KeyboardInterrupt:
                print("\nInterrupted by user!")
            finally:
                sleep(3)
                continue
    finally:
        driver.quit()
        new_chrome.terminate()
        new_chrome.wait()
        exit("Exiting.")




