#!/usr/bin/python3
""" A flask app. """
from flask import Flask


HBNB = Flask(__name__)


@HBNB.route('/', strict_slashes=False)
def display():
    """ Displaying message."""
    return 'Hello HBNB!'


@HBNB.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """ Displaying message of hbnb."""
    return 'HBNB'


@HBNB.route('/c/<text>', strict_slashes=False)
def display_c_user(text):
    """ Displaying message of user."""
    text = text.replace('_', ' ')
    return 'C' + " " + text


if __name__ == '__main__':
    HBNB.run(host="0.0.0.0", port=5000)
