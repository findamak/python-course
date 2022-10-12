from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os

chrome_driver_path = os.environ.get("DRIVER_PATH")
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)
URL = "http://orteil.dashnet.org/experiments/cookie/"
driver.get(URL)

cookie = driver.find_element(By.ID, "cookie")
five_seconds = time.time() + 5
five_minutes = time.time() + 300
while time.time() < five_minutes:
    cookie.click()
    if five_seconds < time.time():
        store = driver.find_elements(By.CSS_SELECTOR, "#store div")
        for item in store[::-1]:
            attribute = item.get_attribute("class")
            if attribute != "grayed" and attribute != "amount":
                item.click()
                break
        five_seconds = time.time() + 5

print(driver.find_element(By.ID, "cps").text)
driver.quit()