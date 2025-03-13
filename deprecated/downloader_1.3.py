from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os, glob, shutil



runtime_path = os.path.realpath(os.path.dirname(__file__))
backup_folder = f"{runtime_path}/backup/"
temp_folder = f"{runtime_path}/temp/"
driver_path = f"{runtime_path}/chromedriver"


options = ChromeOptions()
prefs = {f"download.default_directory" : temp_folder}
options.add_experimental_option("prefs", prefs)
options.add_argument("--headless")
options.add_argument("--blink-settings=imagesEnabled=false")
options.page_load_strategy = "eager"
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(options=options, service=service)
wait = WebDriverWait(driver, timeout=30)


def clean_up():
    """
    Removes old failed downloads and backs up completed downloads
    so ods_graph script will only see new files
    """
    os.chdir(path=temp_folder)
    files = glob.glob("*")
    for file in files:
        if (file.endswith(".crdownload")) or (file.endswith(".log")):
            os.remove(file)
            print("Removed:", file)
        elif (file.endswith(".xls")) or (file.endswith(".xlsx")):
            shutil.move(file, backup_folder + file)
            print("Backed up:", file)


def download_wait(directory, timeout, file_number=None):
    """
    Waits for download to complete successfuly
    """
    seconds = 0
    wait = True
    while wait and (seconds < timeout):
        sleep(1)
        wait = False
        files = os.listdir(directory)
        if (file_number and len(files)) != file_number:
            wait = True

        for file in files:
            if file.endswith(".crdownload"):
                wait = True
        seconds += 1
    return seconds


def downloader(url):
    """
    Downloads new predespacho documents
    """
    try:
        driver.get(url["url"])
        sleep(5)
        wait.until(EC.element_to_be_clickable(driver.find_element(By.CSS_SELECTOR, selector))).click()
        sleep(5)
        total = download_wait(directory=temp_folder, timeout=60)
        if total == 60:
            raise Exception
        else:
            print(url["name"] + f" downloaded in {total} second(s).")
    except:
        print(url["name"] + " not downloaded.")
    finally:
        sleep(1)



if __name__ ==  "__main__":
    selector = "#\\36 9268077341239605_orig > tbody > tr:nth-child(2) > td:nth-child(2) > a"
    urlF = {
        "url" : "https://otr.ods.org.hn:3200/odsprd/f?p=110:4:::::p4_id:4",
        "name" : "Predespacho Final"
    }

    urlS = {
        "url" : "https://otr.ods.org.hn:3200/odsprd/f?p=110:4:::::p4_id:5",
        "name" : "Programación Semanal"
    }
    clean_up()
    for i in (urlF, urlS):
        downloader(url=i)
    driver.quit()

