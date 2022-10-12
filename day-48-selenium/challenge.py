from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

chrome_driver_path = os.environ.get("DRIVER_PATH")
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)
URL = "https://secure-retreat-92358.herokuapp.com/"


driver.get(URL)

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Bill")
last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Gates")
email = driver.find_element(By.NAME, "email")
email.send_keys("billgates@bill.gates")
submit = driver.find_element(By.CSS_SELECTOR, ".btn-primary.btn-block")
submit.send_keys(Keys.ENTER)