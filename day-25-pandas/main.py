# import csv

# # Extract temperatures into list as integers.
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)


# import pandas
#
# # Do the same as above but with the pandas library.
# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
#
# # Play with other conversion methods
# data_dict = data.to_dict()
# temp_list = data["temp"].to_list()
#
# print(data_dict)
# print(temp_list)
#
# # calculate the average of the temp_list using builtin statistics
# print(data["temp"].mean())
# print(data["temp"].max())

# # Get data in columns. Pandas automatically converts columns to attribute.
# print(data.condition)

# Get data in row that matches a search
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# print(monday.condition)
# print(monday.temp)

# Create a dataframe from a dictionary and save to file
# data_dict = {
#     "students": ["Alice", "John", "Bob"],
#     "scores": [76, 45, 67]
# }
# data_table = pandas.DataFrame(data_dict)
# print(data_table)
# data_table.to_csv("new_data.csv")

#TODO: Squirrel Data analysis. Create a csv file with the count of the total nummber of gray, cinnamon, black squirrels.

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cin_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, cin_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")

