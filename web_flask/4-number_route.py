#!/usr/bin/python3
"""
This script  starts a Flask web application
listening in port 0.0.0.0
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ” followed by the value of the text variable
/python/<text>: display “Python ”, followed by the value of the text
/number/<n>: display “n is a number” only if n is an integer
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ returns Hello HBNB!"""
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ returns HBNB """
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def c(text="is cool"):
    """ returns a string """
    return (f'C {text}', (text.replace("_" " ")))


@app.route('/python/<text>')
def python(text="is cool"):
    """ Returns an inputed string """
    return (f'Python {text}', (text.replace("_" " ")))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ Returns "n is a number" if n is an integer """
    if isinstance(n, int):
        return (f'{n} is a number')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
