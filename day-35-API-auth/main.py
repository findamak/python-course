import requests
# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

account_sid = os.environ.get("ACCOUNT_SID")
# Set keys into an environment variable
auth_token = os.environ.get("AUTH_TOKEN")
owm_api_key = os.environ.get("OWM_API_KEY")

parameters = {
    "lat": -33.868820,
    "lon": 151.209290,
    "appid": owm_api_key
}

# need to register a credit card to get access to onecall. Not doing this.
endpoint = "https://api.openweathermap.org/data/3.0/onecall"
# endpoint = "https://api.openweathermap.org/data/2.5/weather"

response = requests.get(endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
# Use the slice function to slice the data we want
weather_slice = weather_data["hourly"][:12]
# Set a boolean variable to change if it will rain
will_rain = False
# Loop through the sliced data
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's raining today, bring an Umbrella",
        from_='+19713206946',
        to='+61458555495'
    )
    print(message.status)