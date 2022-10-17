from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
import time

URL = "https://www.linkedin.com/jobs/search/?currentJobId=3291489126&distance=25&f_AL=true&geoId=105344349&keywords=python%20developer&location=Sydney%2C%20New%20South%20Wales%2C%20Australia&refresh=true&sortBy=R"

chrome_driver_path = os.environ.get("DRIVER_PATH")
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get(URL)

# click the sign in button
click_link = driver.find_element(By.CSS_SELECTOR, "body > div.base-serp-page > header > nav > div > a.nav__button-secondary.btn-md.btn-secondary-emphasis")
click_link.click()
time.sleep(2)

# enter username and password
username = driver.find_element(By.ID, "username")
username.send_keys(os.environ.get("USERNAME"))
password = driver.find_element(By.ID, "password")
password.send_keys(os.environ.get("PASSWORD"))
signin_button = driver.find_element(By.CSS_SELECTOR, "#organic-div > form > div.login__form_action_container > button")
signin_button.click()

# put search results into a list
results = driver.find_elements(By.CSS_SELECTOR, ".ember-view.jobs-search-results__list-item")

for result in results:
    for x in result.find_elements(By.TAG_NAME, "a"):
        print(f"{x.text}: {x.get_attribute('href')}")

driver.quit()

