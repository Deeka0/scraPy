from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, os, glob, shutil



runtime_path = os.path.realpath(os.path.dirname(__file__))
backup_folder = runtime_path + "/backup/"


def clean_up():
    """
    Removes old failed downloads and backs up completed downloads
    so ods_graph script will only see new files
    """
    os.chdir(path=runtime_path)
    files = glob.glob("*")
    for file in files:
        if (file.endswith(".crdownload")) or (file.endswith(".log")):
            os.remove(file)
            print("Removed:", file)
        elif (file.endswith(".xls")) or (file.endswith(".xlsx")):
            shutil.move(file, backup_folder + file)
            print("Backed up:", file)


# checks download fails

def download_wait(directory, timeout, file_number=None):
    """
    Waits for download to complete successfuly
    """
    seconds = 0
    wait = True
    while wait and (seconds < timeout):
        time.sleep(1)
        wait = False
        files = os.listdir(directory)
        if (file_number and len(files)) != file_number:
            wait = True

        for file in files:
            if file.endswith(".crdownload"):
                wait = True
        seconds += 1
    return seconds


urlF = {
    "url" : "https://otr.ods.org.hn:3200/odsprd/f?p=110:4:::::p4_id:4",
    "name" : "Predespacho Final",
    "link" : "#\\36 9268077341239605_orig > tbody > tr:nth-child(2) > td:nth-child(2) > a"
}

urlS = {
    "url" : "https://otr.ods.org.hn:3200/odsprd/f?p=110:4:::::p4_id:5",
    "name" : "Programación Semanal",
    "link" : "#\\36 9268077341239605_orig > tbody > tr:nth-child(2) > td:nth-child(2) > a"
}

tic = time.time()
options = ChromeOptions()
prefs = {f"download.default_directory" : runtime_path}
options.add_experimental_option("prefs", prefs)
options.add_argument("--incognito")
options.add_argument("--headless")
options.add_argument("--blink-settings=imagesEnabled=false")
options.page_load_strategy = "eager"
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, timeout=30)
print(f"Browser opening time: {time.time() - tic} seconds")


def downloader(url):
    """
    Downloads new predespacho documents
    """
    try:
        tic = time.time()
        driver.get(url["url"])
        time.sleep(5)
        print(f"URL load time: {time.time() - tic} seconds")
        wait.until(EC.element_to_be_clickable(
            driver.find_element(By.CSS_SELECTOR, url["link"])
        )).click()
        time.sleep(5)
        total = download_wait(directory=runtime_path, timeout=60)
        if total == 1:
            print(url["name"] + f" downloaded in {total} second.")
        elif total == 60:
            raise Exception
        else:
            print(url["name"] + f" downloaded in {total} seconds.")
    except:
        print(url["name"] + " not downloaded.")
    finally:
        time.sleep(1)




if __name__ ==  "__main__":
    clean_up()
    a = [urlF,urlS]
    for i in a:
        tic_i = time.time()
        downloader(i)
        print("Runtime for " +  i["name"] + f": {time.time() - tic_i} seconds")
    driver.quit()

