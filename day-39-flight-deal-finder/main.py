#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve
# the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

MY_CITY = "Sydney"

# Create spreadsheet object
spreadsheet_object = DataManager()

# Create flight search object
flight_object = FlightSearch()

# Get data from spreadsheet
sheet_data = spreadsheet_object.get_sheety_data()
print(sheet_data)

# Loop through each row in spreadsheet
for item in sheet_data:
    # Check if the IATA code is missing. If so, get the code and populate the
    # spreadsheet.
    if "iataCode" not in item or item["iataCode"] == "":
        city_iata_code = flight_object.get_iata_code(item["city"])
        spreadsheet_object.put_iata_code(city_iata_code, item["id"])

    # Check if fields lowestprice and maxstopovers is missing.
    elif "lowestPrice" not in item or item["lowestPrice"] == "" or "maxStopOvers" not in item \
            or item["maxStopOvers"] == "":
        print(f"Destination city: {item['city']}, does not have lowest price or max stop overs set")

    else:

        search_data = flight_object.get_flights(item["iataCode"], item["lowestPrice"], item["maxStopOvers"])

        try:
            # Create data format object
            flight_data_object = FlightData(search_data)
        except IndexError:
            print(f"No flights found to {item['city']}({item['iataCode']}).")
        else:
            # Print specific search results
            print(
                f"Low price alert! Only ${flight_data_object.adults_price} to fly from "
                f"{MY_CITY}-{flight_data_object.from_airport} "
                f"(Flight:{flight_data_object.outbound_airline}-{flight_data_object.outbound_airline_flight})"
                f" to "
                f"{flight_data_object.dest_city}-{flight_data_object.to_airport} "
                f"(Flight:{flight_data_object.return_airline}-{flight_data_object.return_airline_flight})"
                f", leaving "
                f"{flight_data_object.depart_date} and returning on {flight_data_object.return_date}."
            )

            # Send notifications via SMS
            # if int(flight_data_object.adults_price) < int(item["lowestPrice"]):
            #     notification_manager = NotificationManager()
            #     notification_manager.send_sms(
            #         message=f"Low price alert! Only ${flight_data_object.adults_price} to fly from "
            #                 f"{item['city']}-{flight_data_object.from_airport} "
            #                 f"(Flight:{flight_data_object.outbound_airline}-{flight_data_object.outbound_airline_flight})"
            #                 f"to "
            #                 f"{flight_data_object.dest_city}-{flight_data_object.to_airport} "
            #                 f"(Flight:{flight_data_object.return_airline}-{flight_data_object.return_airline_flight})"
            #                 f", from "
            #                 f"{flight_data_object.depart_date} to {flight_data_object.return_date}."
            #     )

