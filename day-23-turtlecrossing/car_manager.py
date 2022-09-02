from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 3
MOVE_INCREMENT = 0


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.color(random.choice(COLORS))
        # No cars should be generated in the top and bottom 50px of the screen
        self.goto(300, random.randint(-240, 240))
        self.x_move = STARTING_MOVE_DISTANCE
        # The car_speed attribute is used to control the speed of the cars
        self.car_speed = 0

    def move(self):
        new_x = self.xcor() - self.x_move - self.car_speed * MOVE_INCREMENT
        self.goto(new_x, self.ycor())


