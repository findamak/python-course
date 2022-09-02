import requests
from datetime import datetime
import os

TOKEN = os.environ.get("TOKEN")
USERNAME = os.environ.get("username")
pixela_endpoint = "https://pixe.la/v1/users"
headers = {
    "X-USER-TOKEN": TOKEN
}

# Setup user account in pixela
# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Setup a graph
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
#
# graph_config = {
#     "id": "graph1",
#     "name": "Time spent coding",
#     "unit": "hrs",
#     "type": "float",
#     "color": "sora"
# }
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


def create_pixel(create_date, data):
    # Create a pixel
    pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"
    # today = datetime(year=2022, month=8, day=30)
    if create_date == "today":
        today = datetime.now().strftime("%Y%m%d")
    else:
        today = create_date

    pixel_config = {
        # https://www.geeksforgeeks.org/python-strftime-function/
        "date": today,
        "quantity": data
    }

    response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
    print(response.text)


def update_pixel(update_date, data):
    # Update a pixel
    # date_to_update = "20220830"
    update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{update_date}"
    data = {
        "quantity": data
    }

    response = requests.put(url=update_pixel_endpoint, json=data, headers=headers)
    print(response.text)


def delete_pixel(delete_date):
    # Delete a pixel
    delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{delete_date}"

    response = requests.delete(url=delete_pixel_endpoint, headers=headers)
    print(response.text)


user_input = input("Do you want to create, update or delete a pixel? ")


if user_input == "create":
    input_date = input("What is the date you want to do this for? e.g today or enter yyyymmdd: ")
    data_update = input("Enter the hours: ")
    create_pixel(input_date, data_update)
elif user_input == "update":
    input_date = input("What is the date you want to do this for? enter yyyymmdd: ")
    data_update = input("Enter the hours: ")
    update_pixel(input_date, data_update)
elif user_input == "delete":
    input_date = input("What is the date you want to do this for? enter yyyymmdd: ")
    delete_pixel(input_date)
