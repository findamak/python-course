import requests
from datetime import datetime
import os

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
SHEETY_KEY = os.environ.get("SHEETY_KEY")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}

sheety_headers = {
    "Authorization": SHEETY_KEY,
    "Content-Type": "application/json"
}

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/4696bd76b019dc32925edf103e057017/myWorkouts/workouts"

user_input = input("Tell me which exercises you did? ")

nutritionix_data = {
    "query":user_input,
    "gender": "male",
    "weight_kg": 85.00,
    "height_cm": 177.00,
    "age": 90
}

date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%H:%M:%S")


response = requests.post(url=nutritionix_endpoint, headers=headers, json=nutritionix_data)
print(response.text)
data = response.json()

# Easier not to use dictionary comprehension as we need to use different key names anyway.
for exercise in data["exercises"]:
    sheety_data = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    print(sheety_data)

    sheety_response = requests.post(url=sheety_endpoint, headers=sheety_headers, json=sheety_data)
    print(sheety_response.text)





