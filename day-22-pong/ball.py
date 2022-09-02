from turtle import Turtle


# create a Ball class that inherits all attributes and methods from the Turtle class
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.turtlesize(stretch_wid=1, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(0, 0)
        # Store the distance to move the ball as attributes, so we can manipulate these to change the ball direction.
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    # Go back to original position and start the ball in the other direction.
    def reset(self):
        self.goto(0, 0)
        self.bounce_x()

