from turtle import Turtle, Screen
from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Australian Cities",["sydney", "perth", "adelaide", "melbourne", "brisbane"], "c")
table.add_column("UK Cities", ["London", "Bath", "Manchester", "", ""], "c")
print(table)

#timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()