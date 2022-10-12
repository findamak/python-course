from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

# Using a "r" in front of the path escapes the "\a" in the path
#chrome_driver_path = r"C:\Users\anthony\chromedriver_win32\chromedriver.exe"
chrome_driver_path = os.environ.get("DRIVER_PATH")
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)
URL = "https://www.python.org/"


driver.get(URL)

# # Page title
# print(driver.title)
#
# # find element by name
# go_button = driver.find_element(By.NAME, "submit")
# print(go_button.tag_name)
#
# # find element by class name
# logo = driver.find_element(By.CLASS_NAME, "python-logo")
# print(logo.text)
#
# # find element by class selector. in this example, it had class="medium-widget blog-widget"
# css = driver.find_element(By.CSS_SELECTOR, ".medium-widget.blog-widget")
# print(css.text)
#
# # find element by xpath
# link = driver.find_element(By.XPATH, '//*[@id="container"]/li[4]/ul/li[11]/a')
# print(link.text)

# Create a dictionary from an unordered list on website
# Use the css selector to find class "event-widget" and then further drill down by tag elements i.e time, li, a
times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
events = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

dict = {}
for i in range(len(times)):
    dict[i] = {
        "time": times[i].text,
        "name": events[i].text
    }

print(dict)
# close a tab
#driver.close()

# quit browser
driver.quit()