import requests
import os

STOCK_NAME = "TSLA"
COMPANY_NAME = "tesla"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_TOKEN = os.environ.get("TWILIO_TOKEN")

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries.
# e.g. [new_value for (key, value) in dictionary.items()]

api_key = os.environ.get("API_KEY")

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": api_key
}

response = requests.get(STOCK_ENDPOINT, params=parameters)
response.raise_for_status()
stock_data = response.json()

stock_data_list = [value for (key, value) in stock_data["Time Series (Daily)"].items()]
yesterday_price = float(stock_data_list[1]["4. close"])
print(yesterday_price)


#TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday_price = float(stock_data_list[2]["4. close"])
print(day_before_yesterday_price)

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.
# Hint: https://www.w3schools.com/python/ref_func_abs.asp

diff = (yesterday_price - day_before_yesterday_price)
up_down = None
if diff > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before
# yesterday.
diff_percent = round((diff / yesterday_price) * 100)
# print(diff_percent)

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if abs(diff_percent) > 2:

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

    #TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    news_api_key = os.environ.get("NEWS_API_KEY")

    news_parameters = {
        "qInTitle": COMPANY_NAME,
        "apikey": news_api_key
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()["articles"]

    #TODO 7. - Use Python slice operator to create a list that contains the first 3 articles.
    # Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    first_three = news_data[:3]

        ## STEP 3: Use twilio.com/docs/sms/quickstart/python
        #to send a separate message with each article's title and description to your phone number.

    #TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    new_list = [f"{STOCK_NAME}: {up_down}{abs(diff_percent)}%\nHeadline: {item['title']}. \nBrief: {item['description']}"
                for item in first_three]
    # print(new_list)

    #TODO 9. - Send each article as a separate message via Twilio.
    from twilio.rest import Client
    client = Client(TWILIO_SID, TWILIO_TOKEN)

    for article in new_list:
        message = client.messages \
            .create(
            body=article,
            from_='+19713206946',
            to='+61458555495'
        )
        print(message.status)


#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

