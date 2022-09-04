import os
import requests

# This class is responsible for talking to the Google Sheet.

sheety_key = os.environ.get("SHEETY_KEY")
sheety_endpoint = "https://api.sheety.co/4696bd76b019dc32925edf103e057017/flightDeals/prices"
sheety_headers = {
    "Authorization": sheety_key,
    "Content-Type": "application/json"
}

class DataManager:
    def __init__(self):
        self.sheety_data = {}

    def get_sheety_data(self):
        response = requests.get(url=sheety_endpoint, headers=sheety_headers)
        sheety_data = response.json()["prices"]
        return sheety_data

    def put_iata_code(self, code, rowid):
        new_url = f"{sheety_endpoint}/{rowid}"
        put_data = {
            "price": {
                "iataCode": code
            }
        }
        response = requests.put(url=new_url, headers=sheety_headers, json=put_data)
        print(f"Post request output:\n{response.text}")
