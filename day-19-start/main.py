from turtle import Turtle, Screen

# Example of higher order functions
# Add
# def add(n1, n2):
#     return n1 + n2
# # subtract
# def subtract(n1, n2):
#     return n1 - n2
# # multiply
# def multiply(n1, n2):
#     return n1 * n2
# # divide
# def divide(n1, n2):
#     return n1 / n2
# def calc(n1, n2, function):
#     return function(n1, n2)
#
# print(calc(5, 3, multiply))

timmy = Turtle()
screen = Screen()
timmy.pencolor("pink")
timmy.pensize(20)

def forward():
    timmy.forward(10)

def backwards():
    timmy.backward(10)

def left():
    timmy.left(10)

def right():
    timmy.right(10)

def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()

screen.listen()
screen.onkey(key="w", fun=forward)
screen.onkey(key="s", fun=backwards)
screen.onkey(key="a", fun=left)
screen.onkey(key="d", fun=right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()