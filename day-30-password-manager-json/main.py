from tkinter import *
# messagebox is not a class but a module, hence we need to import it.
from tkinter import messagebox
import pyperclip
import json
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
    new_data = {
        website: {
            "username": username,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0 or len(username) == 0:
        messagebox.showinfo(title="Oops", message="Ensure all fields are not empty.")
    else:
        try:
            # Try to get data from existing file
            with open("data.json", "r") as data_file:
                # Read data from a json file. Open file as "r". "Data" is just a python dictionary.
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # If everything in the try block succeeds, add new data to existing data
            data.update(new_data)
            # Open file in "w" mode to write to it
            with open("data.json", "w") as data_file:
                # Add new data to json file with indents so it is easier to read
                json.dump(data, data_file, indent=4)
        finally:
            # Delete entry fields from character 0 to the 'END'. 'END' is a builtin tkinter constant.
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD -------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data stored in password manager.")
    else:
        if website in data:
            username = data[website]["username"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Username: {username}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message="Website not stored in password manager.")

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
website_entry = Entry(width=34)
website_entry.grid(row=1, column=1)
# Focus cursor in this entry
website_entry.focus()
username_entry = Entry(width=52)
username_entry.grid(row=2, column=1, columnspan=2)
# Pre-populate this entry
username_entry.insert(0, "something@something.com")
password_entry = Entry(width=34)
password_entry.grid(row=3, column=1)

# Setup buttons
search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(row=1, column=2)
generate_button = Button(text="Generate Password", width=14, highlightthickness=0, command=generate_password)
generate_button.grid(row=3, column=2)
add_button = Button(text="Add", width=45, highlightthickness=0, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
