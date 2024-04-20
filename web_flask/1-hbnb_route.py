#!/usr/bin/python3
""" A flask route."""
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


if __name__ == '__main__':
    HBNB.run(host="0.0.0.0", port=5000)
