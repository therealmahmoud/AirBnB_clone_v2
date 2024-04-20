#!/usr/bin/python3
""" A flask route."""
from flask import Flask

HBNB = Flask(__name__)

@HBNB.route('/', strict_slashes=False)
def display():
    """ Displaying message."""
    return 'Hello HBNB!'

def display():
    """ Displaying message."""
    return 'Hello HBNB!'