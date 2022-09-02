import tkinter

# Create window
window = tkinter.Tk()
window.title("Mile to Km converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

# Create entry
miles_input = tkinter.Entry(width=15)
miles_input.insert(tkinter.END, string="0")
miles_input.grid(row=0, column=1)

# Create "is equal to" label
equal_label = tkinter.Label(text="is equal to", font=("Arial", 14))
equal_label.grid(row=1, column=0)

# Create "miles" label
miles_label = tkinter.Label(text="Miles", font=("Arial", 14))
miles_label.grid(row=0, column=2)

# Create "Km" label
km_label = tkinter.Label(text="Km", font=("Arial", 14))
km_label.grid(row=1, column=2)

# Create output label
output = tkinter.Label(text=0, font=("Arial", 14))
output.grid(row=1, column=1)


def conversion():
    miles = float(miles_input.get())
    km = miles * 1.689
    output.config(text=f"{km}")


# Create calculate button
button = tkinter.Button(text="Calculate", command=conversion)
button.grid(row=2, column=1)

window.mainloop()