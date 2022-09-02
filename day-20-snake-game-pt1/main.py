from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)
game_is_on = True

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Set arrow keys to control the snake direction
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    # This controls the time between screen updates so also controls the speed on movement.
    time.sleep(0.9)

    # To control where the snake goes, we control the movements of the first segment i.e segment[0] and the segments
    # after will follow.
    snake.move()

    # Detect collision with food. Food size is 10. Choosing 15 gives a buffer.
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        scoreboard.update_score()
        food.refresh()
        snake.extend()

    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # game_is_on = False
        # scoreboard.game_over()
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail. The first segment is the snake head so we need to bypass this. Slicing by [1:]
    # does this.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # game_is_on = False
            # scoreboard.game_over()
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
