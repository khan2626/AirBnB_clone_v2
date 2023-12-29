#!/usr/bin/python3
"""
This script  starts a Flask web application
listening in port 0.0.0.0
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ” followed by the value of the text variable 
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return ("Hello HBNB!")

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return ("HBNB")

@app.route('/c/<text>')
def c(text=None):
    return f'C {text}'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
