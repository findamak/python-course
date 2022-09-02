from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Create the screen object.
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

# Turn off the screen animation
screen.tracer(0)

# Create objects
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()


# Function to quit game
def quitgame():
    global game_is_on
    game_is_on = False


screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkey(quitgame, "q")

time_value = 0.1
game_is_on = True


while game_is_on:

    # This controls the time between screen updates so also controls the speed of movement.
    time.sleep(time_value)

    screen.update()
    ball.move()

    # Detect collision with top or bottom wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles.
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Detect if ball goes out of bounds
    if ball.distance(r_paddle) > 50 and ball.xcor() > 400:
        # Add a point to the other player.
        scoreboard.increase_l_score()
        scoreboard.update_score()
        # Reset ball to center and start moving ball towards other player and increase ball speed.
        ball.reset()
        if time_value > 0.01:
            time_value -= 0.01

    if ball.distance(l_paddle) > 50 and ball.xcor() < -400:
        # Add a point to the other player.
        scoreboard.increase_r_score()
        scoreboard.update_score()
        # Reset ball to center and start moving ball towards other player and increase ball speed.
        ball.reset()
        if time_value > 0.01:
            time_value -= 0.01



screen.exitonclick()