from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

chrome_driver_path = os.environ.get("DRIVER_PATH")
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)
URL = "https://en.wikipedia.org/wiki/Main_Page"


driver.get(URL)

# # Get article count solution 1
# counts = driver.find_elements(By.ID, "articlecount")
# list = [count.text for count in counts]
# print(list[0].split()[0])

# Get article count solution 2. # is the CSS selector for ID
counts = driver.find_elements(By.CSS_SELECTOR, "#articlecount a")
list = [count.text for count in counts]
print(list[0])

# Clicking
click_link = driver.find_element(By.LINK_TEXT, "encyclopedia")
click_link.click()

# Typing and using keyboard keys
search = driver.find_element(By.NAME, "search")
search.send_keys("python")
search.send_keys(Keys.ENTER)

# quit browser
# driver.quit()