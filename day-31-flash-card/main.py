from tkinter import *
import pandas
import random

# To create the "<foreign_language.csv>" file, copy the words from
# "https://github.com/hermitdave/FrequencyWords/tree/master/content/2018"
# then put this into Excel and use the "data -> text to columns" function to separate the word and frequency number into
# separate columns. Then copy the foreign word column into a Google sheet. Then use Google's
# "=GOOGLETRANSLATE(<cell of foreign word>,"zh-tw","en")" excel function to translate the words into english. Do this
# for all the words. Then save the file as a csv.

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
LANGUAGE = "Chinese"
LANGUAGE_FILE = "data/500_chinese_words.csv"
TIMER = 3000
random_word = {}
data_dict_to_learn = {}

# ---------------------------- DATA ----------------------------------- #
try:
    dataframe = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_dataframe = pandas.read_csv(LANGUAGE_FILE)
    data_dict_to_learn = original_dataframe.to_dict(orient="records")
else:
    data_dict_to_learn = dataframe.to_dict(orient="records")


# ---------------------------- FUNC ----------------------------------- #
def choose_word():
    global random_word, timer
    # cancel any previous timers we started.
    window.after_cancel(timer)
    # choose a random foreign word
    random_word = (random.choice(data_dict_to_learn))
    foreign_word = random_word[LANGUAGE]
    # display the front of the card with this new foreign word
    canvas.itemconfig(canvas_image, image=front_img)
    canvas.itemconfig(language_text, text=LANGUAGE, fill="black")
    canvas.itemconfig(word_text, text=foreign_word, fill="black")
    timer = window.after(TIMER, func=show_english_word)


def show_english_word():
    # get existing random word we chose and display the corresponding english word
    global random_word
    english_word = random_word["English"]
    canvas.itemconfig(canvas_image, image=back_img)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=english_word, fill="white")


def word_known():
    data_dict_to_learn.remove(random_word)
    data = pandas.DataFrame(data_dict_to_learn)
    # Don't add index to the new csv. If we included indexes, it would add new indexes in everytime we saved the file.
    data.to_csv("data/words_to_learn.csv", index=False)
    choose_word()

# ---------------------------- UI SETUP ------------------------------- #

# Setup window


window = Tk()
window.title("Flash card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


# Setup canvas
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
# create_image takes (x, y, image) tuple. x, y is the centre in this case.
canvas_image = canvas.create_image(400, 263, image=front_img)
language_text = canvas.create_text(400, 150, text="", font=LANGUAGE_FONT)
word_text = canvas.create_text(400, 263, text="", font=WORD_FONT)
canvas.grid(row=0, column=0, columnspan=2)

# Setup buttons. Tick means we know the word already. Cross means we don't know the word yet.
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=word_known)
right_button.grid(row=1, column=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=choose_word)
wrong_button.grid(row=1, column=0)

# ---------------------------- Run ---------------------------------- #

# Start timer to then show english translation after TIMER seconds. "timer" needs to be defined before we call
# choose_word as we use "timer" inside "choose_word"
timer = window.after(TIMER, func=show_english_word)

# Call choose_word() to populate the first card
choose_word()


window.mainloop()
