import os
import requests
from datetime import datetime, timedelta
# This class is responsible for talking to the Flight Search API.

# Number of days from today to search from.
DAYS_FROM = 1
# Max number of days from today to search from.
DAYS_TO = 180
# Number of days from today for return flight
RETURN_FROM = 7
# Max number of days from today for return flight
RETURN_TO = 28
# Currency
CURR = "AUD"
# City IATA code we fly from
CITY = "city:SYD"
# Flight type can be "oneway" or "round"
FLIGHT_TYPE = "round"
# the minimal length of stay in the destination
NIGHTS_FROM = 7
# the maximal length of stay in the destination
NIGHTS_TO = 28

kiwi_key = os.environ.get("KIWI_KEY")
kiwi_endpoint = "https://tequila-api.kiwi.com"
search = f"{kiwi_endpoint}/v2/search"
location = f"{kiwi_endpoint}/locations/query"
headers = {
    "accept": "application/json",
    "apikey": kiwi_key
}

class FlightSearch:

    def get_iata_code(self, city_input):
        params = {
            "term": city_input,
            "location_types": "city",
            "active_only": "true"
        }
        response = requests.get(url=location, headers=headers, params=params)
        data = response.json()
        print(f"IATA code for {city_input}: {data['locations'][0]['code']}")
        return data["locations"][0]["code"]

    def get_flights(self, destination_code, price, max_stop):

        date_from = (datetime.now() + timedelta(days=DAYS_FROM)).strftime("%d/%m/%Y")
        date_to = (datetime.now() + timedelta(days=DAYS_TO)).strftime("%d/%m/%Y")
        #return_from = (datetime.now() + timedelta(days=RETURN_FROM)).strftime("%d/%m/%Y")
        #return_to = (datetime.now() + timedelta(days=RETURN_TO)).strftime("%d/%m/%Y")

        params = {
            "fly_from": CITY,
            "fly_to": destination_code,
            "date_from": date_from,
            "date_to": date_to,
            #"return_from": return_from,
            #"return_to": return_to,
            "price_to": price,
            "max_stopovers": max_stop,
            "curr": CURR,
            "flight_type": FLIGHT_TYPE,
            "nights_in_dst_from": NIGHTS_FROM,
            "nights_in_dst_to": NIGHTS_TO,
            "one_for_city": 1,
            "selected_cabins": "M",
            "limit": "50"
        }

        response = requests.get(url=search, headers=headers, params=params)
        search_data = response.json()
        return search_data
