#!/usr/bin/python3
""" A flask route """
from flask import Flask

HBNB = Flask(__name__)


@HBNB.route('/')
def display():
    """ Displaying Message."""
    return 'Hello HBNB!'


if __name__ == '__main__':
    HBNB.run()
