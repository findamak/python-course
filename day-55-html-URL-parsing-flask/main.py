from flask import Flask
app = Flask(__name__)

# Functions to add HTML tags
def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

# This is known as a python decorator function
@app.route('/')
def hello_world():
    # Inline HTML
    return '<h1>Hello, World!</h1>' \
           '<p>This is a kitten</p>' \
           '<img src=https://media.giphy.com/media/K1tgb1IUeBOgw/giphy.gif>'

# Decorate the bye() function with the @app, @make_* decorators to apply HTML tags
@app.route('/bye')
@make_bold
@make_underlined
@make_emphasis
def bye():
    return "Bye!"

# Pass variables via the URL to the function
@app.route('/<name>/<int:number>')
def greet(name, number):
    return f"Hello {name}, you are {number} years old."

# This allows us to run this application without having to set a windows environment variable using
# '$env:FLASK_APP = "hello.py"' and then typing flask run in the command line. Running this file will start the server.
if __name__ == "__main__":
    # Turn on debug which also reloads the webserver whenever changes are made to this file.
    app.run(debug=True)