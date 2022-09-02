from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        # This is used to display on the scoreboard as well as control car speed.
        self.level = 0

    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
        # Once the finish line is reached:
        if self.ycor() == FINISH_LINE_Y:
            # Set the level to +1.
            self.level += 1
            # Go back to the start
            self.goto(STARTING_POSITION)




