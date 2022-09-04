
#This class is responsible for structuring the flight data.

class FlightData:

    def __init__(self, data):
        self.adults_price = data["data"][0]["fare"]["adults"]
        self.children_price = data["data"][0]["fare"]["children"]
        self.infants_price = data["data"][0]["fare"]["infants"]
        # Route 0 is the outbound flight. Route 1 is the return flight
        self.dest_city = data["data"][0]["route"][0]["cityTo"]
        self.dest_city_code = data["data"][0]["route"][0]["cityCodeTo"]
        self.from_airport = data["data"][0]["route"][0]["flyFrom"]
        self.to_airport = data["data"][0]["route"][0]["flyTo"]
        self.outbound_airline = data["data"][0]["route"][0]["airline"]
        self.outbound_airline_flight = data["data"][0]["route"][0]["flight_no"]
        self.depart_date = data["data"][0]["route"][0]["local_departure"].split("T")[0]
        self.return_date = data["data"][0]["route"][1]["local_departure"].split("T")[0]
        self.return_airline = data["data"][0]["route"][1]["airline"]
        self.return_airline_flight = data["data"][0]["route"][1]["flight_no"]


