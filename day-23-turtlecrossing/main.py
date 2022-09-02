import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Create the screen
screen = Screen()
screen.setup(width=600, height=600)
# Turn off animation
screen.tracer(0)
screen.title("Turtle crossing the road game")

# List to store car objects
all_cars = []

# Create a turtle player that starts at the bottom of the screen and listen for the "Up" keypress to move the turtle
# north
turtle = Player()
screen.listen()
screen.onkey(turtle.move, "Up")

# Initialise the scoreboard
scoreboard = Scoreboard()

game_is_on = True
car_count = 0

while game_is_on:
    time.sleep(0.1)
    screen.update()
    # Set the scoreboard level to the same as the "turtle.level" attribute as we increase the level in player.py
    scoreboard.score = turtle.level
    scoreboard.update_level()
    # HINT was to generate a new car only every 6th time the game loop runs.
    car_count += 1
    if car_count % 6 == 0:
        car = CarManager()
        all_cars.append(car)
    # For each car created:
    for each_car in all_cars:
        # Set car speed attribute to the turtle level
        each_car.car_speed = turtle.level
        # Move car
        each_car.move()
        # Detect if turtle has collided with car
        if turtle.distance(each_car) < 25:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
