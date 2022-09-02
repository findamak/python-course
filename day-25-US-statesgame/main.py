import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

draw_turtle = turtle.Turtle()
draw_turtle.penup()
draw_turtle.hideturtle()
draw_turtle.color("black")
FONT = ("Courier", 10, "normal")


# This code can help you provide x and y co-ordinates of where you click your mouse. Angela used this to populate the
# co-ordninates in the 50_states.csv file.
# def mouse_click_coords(x, y):
#     print(x, y)
# turtle.onscreenclick(mouse_click_coords)
# turtle.mainloop()

score = 0

data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()
game_is_on = True
# Store all correct guesses in a list.
correct_guesses = []
screen_title = "Guess the state"

while game_is_on:
    # Store the users guess.
    answer_state = screen.textinput(title=screen_title, prompt="What's another states name?").title()

    # Give the user an option to exit the game
    if answer_state == "Exit":
        break
    # Check if the guess is among the 50 states.
    if answer_state in states_list:
        score += 1
        screen_title = f"{score}/50 States Correct"
        correct_guesses.append(answer_state)
        row_data = data[data.state == answer_state]
        x = int(row_data.x)
        y = int(row_data.y)
        draw_turtle.goto(x, y)
        # item method: https://pandas.pydata.org/docs/reference/api/pandas.Series.item.html. We could have also just
        # used answer_state as well.
        draw_turtle.write(row_data.state.item(), align="center", font=FONT)
        if score == 50:
            game_is_on = False

# Create a csv of all states that were not guessed by the user.

# missed_states = []
# for state in states_list:
#     if state not in correct_guesses:
#         missed_states.append(state)
# The above can be replaced with the below conditional list comprehension
missed_states = [state for state in states_list if state not in correct_guesses]
serial_data = pandas.Series(missed_states)
serial_data.to_csv("missing_states.csv")


# Below is no longer needed as we now have a break to exit game.
#screen.exitonclick()