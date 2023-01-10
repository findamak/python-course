from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

# This allows us to run this application without having to set a windows environment variable using
# '$env:FLASK_APP = "hello.py"' and then typing flask run in the command line. Running this file will start the server.
if __name__ == "__main__":
    # Turn on debug which also reloads the webserver whenever changes are made to this file.
    app.run(debug=True)
