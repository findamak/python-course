from turtle import Screen
import turtle as t
import random

timmy = t.Turtle()
timmy.shape("turtle")
timmy.color("blue")
timmy.speed('fastest')

# Draw a square
# for _ in range(4):
#     timmy.forward(100)
#     timmy.left(90)

# Draw a dashed line
# for _ in range(4):
#     timmy.pendown()
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)


# Draw different shapes
# colours = ["red", "blue", "green", "orange", "purple", "violet", "pink", "yellow", "brown", "aqua"]
#
#
# def draw_shape(sides):
#     for _ in range(sides):
#         timmy.forward(100)
#         timmy.right(360 // sides)
#
#
# for number_sides in range(3, 11):
#     timmy.pencolor(random.choice(colours))
#     draw_shape(number_sides)

# Generate random RGB colours
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour

# Generate a random walk
# #colours = ["red", "blue", "green", "orange", "purple", "violet", "pink", "yellow", "brown", "aqua"]
# direction = [90, 180, 270, 360]
# timmy.pensize(10)
#
# def random_walk():
#     #pen_color = random.choice(colours)
#     #timmy.pencolor(pen_color)
#     timmy.pencolor(random_color())
#     angle = random.choice(direction)
#     timmy.setheading(angle)
#     timmy.forward(50)
#
#
# for _ in range(40):
#     random_walk()

# Draw a spirograph
timmy.pencolor(random_color())
angle = 0
# number_of_circles needs to be less that 360
number_of_circles = 359
for _ in range(number_of_circles):
    timmy.pencolor(random_color())
    angle += int(360 / number_of_circles)
    timmy.setheading(angle)
    timmy.circle(100)


screen = Screen()
screen.exitonclick()
