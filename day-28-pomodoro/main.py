from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
tick_text = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_button_action():
    # reset the timer
    window.after_cancel(timer)
    # reset the timer text
    canvas.itemconfig(timer_text, text="00:00")
    # reset title label
    timer_label.config(text="Timer")
    # reset the check marks and reps
    global tick_text
    tick_text = ""
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    global timer_label
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # If its 8th rep
    if reps % 8 ==0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    # If its 2nd/4th/6th rep
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        # If its 1st/3rd/5th/7th rep
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global reps
    global tick_label
    global tick_text

    # Edit text in canvas
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        # Dynamic typing to make it display "00" to look like a clock
        count_sec = f"0{count_sec}"

    # reconfigure the timer text to display in human friendly format
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        # After 1000ms, execute "count_down" function and subtract one from the count. This is how we actually count
        # down.
        global timer
        timer = window.after(1000, count_down, count - 1)
    # start timer automatically once it reaches 0
    else:
        start_timer()
        if reps % 2 == 0:
            tick_text += "✔"
            tick_label.config(text=tick_text)


# ---------------------------- UI SETUP ------------------------------- #

# Setup window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Setup canvas with tomato image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Timer label
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
timer_label.grid(row=0, column=1)

# Start button
start_button = Button(text="start", command=start_timer, highlightthickness=0)
start_button.grid(row=2, column=0)


# Reset button
reset_button = Button(text="reset", command=reset_button_action, highlightthickness=0)
reset_button.grid(row=2, column=2)


# Green tick label. We don't add a tick until we have completed a work session.
tick_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
tick_label.grid(row=2, column=1)

window.mainloop()
