from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time

def launch():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

def clickbutton(driver, number):
    try:
        button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[text()='{}']".format(number))))
        button.click()
    except Exception as e:
        print(e)
    return 1


def getElementByXpathOrWait(driver, element_xpath, delay, timeoutmsg):
    try:
        return WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, element_xpath)))
    except TimeoutException:
        print("Timeout error ({} seconds). {}".format(delay, timeoutmsg))
        return None
    
def waitInseconds(seconds):
    for i in range(1,seconds+1):
        print(i)


def main():
    driver = launch()
    driver.get("https://zzzscore.com/1to50/en/")
    total_height = driver.execute_script("return document.body.scrollHeight")
    driver.execute_script("window.scrollTo(0, arguments[0]);", total_height/4)
    time.sleep(0.5)
    for i in range(1, 51):
        clickbutton(driver, i)
    print("Done!")

if __name__ == "__main__":
    main()