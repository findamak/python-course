# import colorgram
#
# colours = colorgram.extract('image.jpg', 10)
# rgb_list = []
# for colour in colours:
#     r = colour.rgb.r
#     g = colour.rgb.g
#     b = colour.rgb.b
#     rgb_list.append((r, g, b))
#
# print(rgb_list)



import turtle as t
from turtle import Screen
import random

timmy = t.Turtle()
timmy.hideturtle()
timmy.shape("turtle")
timmy.color("blue")
timmy.speed('fastest')
timmy.pensize(20)
t.colormode(255)
space = 50

# Get turtle to starting position
timmy.penup()
timmy.backward(200)
timmy.setheading(-90)
timmy.forward(200)
timmy.setheading(0)


color_list = [(121, 96, 85), (188, 160, 123), (71, 99, 123), (132, 73, 87),
              (69, 107, 91), (130, 158, 172), (182, 140, 152), (136, 166, 154)]

def paint_forward():
    timmy.pendown()
    timmy.dot(20, random.choice(color_list))
    timmy.penup()
    timmy.forward(space)

def next_position():
    timmy.penup()
    timmy.setheading(90)
    timmy.forward(space)
    timmy.setheading(180)
    timmy.forward(space * 10)
    timmy.setheading(0)


# Create painting with 10 x 10 of spots. Each dot is 20 in size and 50 spaces between.
for _ in range(10):
    for _ in range(10):
        paint_forward()
    next_position()


screen = Screen()
screen.exitonclick()