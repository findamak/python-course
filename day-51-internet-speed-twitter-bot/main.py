import os
from internetspeedbot import InternetSpeedTwitterBot

PROMISED_DOWN = 60
PROMISED_UP = 10

internet_speed = InternetSpeedTwitterBot()

internet_speed.get_internet_speed("https://www.speedtest.net/")
internet_speed.tweet_at_provider("https://exetel.com.au", PROMISED_DOWN, PROMISED_UP)


