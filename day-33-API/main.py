import requests

# ISS example
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# # Raise for status responds with the actual error code if one is received.
# response.raise_for_status()
# # Get the actual json data received
# data = response.json()
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# iss_position = (longitude, latitude)
# print(iss_position)

# Sunrise and sunset example. https://sunrise-sunset.org/api. Use latlong.net to get co-ords for a location.

from datetime import datetime

# Sydney co-ords.
LAT = -33.868820
LNG = 151.209290

parameters = {
    "lat": LAT,
    "lng": LNG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

# Get hour for the sunrise and sunset times. Times are in UTC.
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise + 10)
print(sunset + 10)

# Get the hour for the current time.
time_now = datetime.now()
print(time_now.hour)