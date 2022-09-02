import tkinter

window = tkinter.Tk()
window.title("Hello tkinter")
window.minsize(width=500, height=500)
# Add padding or blank space to window edges
window.config(padx=20, pady=20)

# Create a label
my_label = tkinter.Label(text="I am a label", font=("Arial", 20, "bold"))
# Display the label on the screen
my_label.pack(side="bottom")
# Change the label "text" parameter
my_label["text"] = "New text"
my_label.config(text="New text")

# Create a button that performs an action

def button_action():
    new_text = input.get()
    my_label.config(text=new_text)

button = tkinter.Button(text="Click me", command=button_action)
button.place(x=0, y=0)

# Input box
input = tkinter.Entry(width=10)
input.place(x=0, y=100)
input2 = tkinter.Entry(width=10)
# Cannot mix pack and grid together to display objects.
# input2.grid(column=0, row=1)

window.mainloop()
