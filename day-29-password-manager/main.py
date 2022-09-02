from tkinter import *
# messagebox is not a class but a module, hence we need to import it.
from tkinter import messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Below code structure was taken from earlier Password Generator Project and simplified using list comprehension.
import random


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Password has between 8 to 10 letters
    nr_letters = random.randint(8, 10)
    # Password has between 2 to 4 symbols
    nr_symbols = random.randint(2, 4)
    # Password has between 2 to 4 numbers
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0 or len(username) == 0:
        messagebox.showinfo(title="Oops", message="Ensure all fields are not empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {username}"
                                                      f"\nPassword: {password}\nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {username} | {password}\n")
                # Delete entry fields from character 0 to the 'END'. 'END' is a builtin tkinter constant.
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# Setup window
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Setup canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
# create_image takes (x, y, image) tuple. x, y is the centre in this case.
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

# Setup labels
website_label = Label(text="website:", )
website_label.grid(row=1, column=0)
username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Setup inputs
website_entry = Entry(width=52)
website_entry.grid(row=1, column=1, columnspan=2)
# Focus cursor in this entry
website_entry.focus()
username_entry = Entry(width=52)
username_entry.grid(row=2, column=1, columnspan=2)
# Pre-populate this entry
username_entry.insert(0, "something@something.com")
password_entry = Entry(width=34)
password_entry.grid(row=3, column=1)

# Setup buttons
generate_button = Button(text="Generate Password", highlightthickness=0, command=generate_password)
generate_button.grid(row=3, column=2)
add_button = Button(text="Add", width=44, highlightthickness=0, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
