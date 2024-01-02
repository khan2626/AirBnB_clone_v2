#!/usr/bin/python3
"""Importing Flask to run a flask app"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.teardown_appcontext
def close(self):
    """ This method closes the session """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Displays a html page with states and cities"""
    states = storage.all(State)
    return render_template('8-cities_by_states.html', Table="States", states=states)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
