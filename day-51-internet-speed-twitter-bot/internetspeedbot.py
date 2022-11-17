from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time


class InternetSpeedTwitterBot:

    def __init__(self):
        self.down = 0
        self.up = 0
        self.chrome_driver_path = os.environ.get("DRIVER_PATH")
        self.service = Service(executable_path=self.chrome_driver_path)
        self.driver = webdriver.Chrome(service=self.service)

    def get_internet_speed(self, url):
        self.driver.get(url)
        # find and click on the "go" button to start the speedtest
        go = self.driver.find_element(By.CSS_SELECTOR, '#container > div > div.main-content > div > div > div > div.pure-u-custom-speedtest > div.speedtest-container.main-row > div.start-button > a')
        go.click()
        # let the test finish. If it takes longer than this time tp finish then we will not get the results
        time.sleep(60)
        # update the attributes with the results of the speedtest
        self.down = self.driver.find_element(By.CSS_SELECTOR, '#container > div > div.main-content > div > div > div > div.pure-u-custom-speedtest > div.speedtest-container.main-row > div.main-view > div > div.result-area.result-area-test > div > div > div.result-container-speed.result-container-speed-active > div.result-container-data > div.result-item-container.result-item-container-align-center > div > div.result-data.u-align-left > span').text
        self.up = self.driver.find_element(By.CSS_SELECTOR, '#container > div > div.main-content > div > div > div > div.pure-u-custom-speedtest > div.speedtest-container.main-row > div.main-view > div > div.result-area.result-area-test > div > div > div.result-container-speed.result-container-speed-active > div.result-container-data > div.result-item-container.result-item-container-align-left > div > div.result-data.u-align-left > span').text
        print(f"down: {self.down}")
        print(f"up: {self.up}")

    def tweet_at_provider(self, company, down, up):
        TWITTER_EMAIL = os.environ.get("TWITTER_EMAIL")
        TWITTER_USERNAME = os.environ.get("TWITTER_USERNAME")
        TWITTER_PASSWORD = os.environ.get("TWITTER_PASSWORD")
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(2)

        # enter email
        email = self.driver.find_element(By.XPATH,
            '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email.send_keys(TWITTER_EMAIL)
        email_button = self.driver.find_element(By.CSS_SELECTOR, '#layers > div > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-14lw9ot.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div > div > div > div:nth-child(6) > div')
        email_button.click()

        # enter username. twitter will prompt for this if it detects strange login behaviour
        time.sleep(2)
        username = self.driver.find_element(By.CSS_SELECTOR, '#react-root > div > div > div > main > div > div > div > div.css-1dbjc4n.r-6koalj.r-16y2uox > div.css-1dbjc4n.r-16y2uox.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div.css-1dbjc4n.r-1fq43b1.r-16y2uox.r-1wbh5a2.r-1dqxon3 > div > div > div.css-1dbjc4n.r-mk0yit.r-1f1sjgu > label > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-xd6kpl.r-1pn2ns4.r-ttdzmv > div > input')
        username.send_keys(TWITTER_USERNAME)
        username_button = self.driver.find_element(By.CSS_SELECTOR, '#react-root > div > div > div > main > div > div > div > div.css-1dbjc4n.r-6koalj.r-16y2uox > div.css-1dbjc4n.r-16y2uox.r-1jgb5lz.r-13qz1uu > div.css-1dbjc4n.r-14lw9ot.r-1p0dtai.r-1d2f490.r-1xcajam.r-zchlnj > div > div > div > div > div > div > span > span')
        username_button.click()

        # enter password
        time.sleep(2)
        password = self.driver.find_element(By.XPATH,
            '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(TWITTER_PASSWORD)
        password_button = self.driver.find_element(By.CSS_SELECTOR, '#layers > div > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-14lw9ot.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div.css-1dbjc4n.r-1isdzm1 > div > div.css-1dbjc4n > div > div > div > div > span > span')
        password_button.click()
        time.sleep(2)

        # click the compose button and enter tweet
        time.sleep(5)
        tweet_compose = self.driver.find_element(By.CSS_SELECTOR,
            '#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > header > div > div > div > div:nth-child(1) > div.css-1dbjc4n.r-1awozwy.r-1p6iasa.r-e7q0ms > a > div')
        tweet_compose.click()
        tweet_input = self.driver.find_element(By.CSS_SELECTOR, '#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div.css-1dbjc4n.r-16y2uox.r-1jgb5lz.r-13qz1uu > div > div > div:nth-child(1) > div > div > div > div > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div.css-1dbjc4n.r-184en5c > div > div > div > div > div > div.css-1dbjc4n.r-16y2uox.r-bnwqim.r-13qz1uu.r-1g40b8q > div > div > div > div > label > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2 > div > div > div > div > div > div.DraftEditor-editorContainer > div > div > div > div')
        tweet = f"Hey {company}, why is my internet speed {self.down}down/{self.up}up when I pay for {down}down/{up}up?"
        tweet_input.send_keys(tweet)
        time.sleep(3)
        tweet_button = self.driver.find_element(By.XPATH,
            '//*[@id="layers"]/div[3]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]')
        tweet_button.click()

        time.sleep(2)
        self.driver.quit()

