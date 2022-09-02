from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "pink", "black"]
all_turtles = []
is_race_on = False


def create_turtle(color, y):
    # FYI, objects do not need unique names.
    # Objects can have the same name. What differentiates them is their state aka, color, position, etc
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(color)
    tim.goto(-230,-100 + y)
    all_turtles.append(tim)

for i in range(len(colors)):
    create_turtle(colors[i], i * 40)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle_name in all_turtles:
        # turtle width is 40. Centre of turtle is 20. its x co-ordinates when it touches the finish line is 250-20=230
        if turtle_name.xcor() > 220:
            is_race_on = False
            # The turtle color is comprised of pencolor and fillcolor i.e turtle.color(pencolor, fillcolor).
            # Using the pencolor works fine.
            winning_color = turtle_name.pencolor()
            if winning_color == user_bet:
                print(f"You've won. The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost. The {winning_color} turtle is the winner!")

        # Randomly move turtle forward
        rand_distance = random.randint(0, 10)
        turtle_name.forward(rand_distance)

screen.exitonclick()