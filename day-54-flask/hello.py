from flask import Flask
app = Flask(__name__)


# This is known as a python decorator function
@app.route('/')
def hello_world():
    return 'Hello, World!'


# This allows us to run this application without having to set a Windows environment variable using
# '$env:FLASK_APP = "hello.py"' and then typing flask run in the command line. Running this file will start the server.
if __name__ == "__main__":
    app.run()
