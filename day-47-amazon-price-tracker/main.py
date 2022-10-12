import requests
import lxml
from bs4 import BeautifulSoup
from notification_manager import NotificationManager

URL = "https://www.amazon.com.au/Dyson-TP07-Purifier-Cool-Tower/dp/B09FDVB3J6/ref=sr_1_5?qid=1665388364"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    "Accept-Language":"en-US,en;q=0.8"
}


request = requests.get(URL, headers=headers)
content = request.text

soup = BeautifulSoup(content, "lxml")
prod_title = soup.find("span", class_="a-size-large product-title-word-break").getText().strip()
print(prod_title)
price_tag = soup.find("span", class_="a-price-whole")
price = float(price_tag.getText().split(".")[0])
print(price)

link = soup.find("link", rel="canonical").get("href")
print(link)

notification_manager = NotificationManager()
notification_manager.send_sms(message=f"Product: {prod_title} is selling for ${price}. Link: {link}")
