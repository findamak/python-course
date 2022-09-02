from turtle import Turtle

Y_MOVE = 20


# create a Paddle class that inherits all attributes and methods from the Turtle class
class Paddle(Turtle):

    def __init__(self, x_pos, y_pos):
        super().__init__()
        # Create paddle object
        self.shape("square")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(x_pos, y_pos)

    # Create methods to control the paddle direction
    def up(self):
        new_y = self.ycor() + Y_MOVE
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - Y_MOVE
        self.goto(self.xcor(), new_y)