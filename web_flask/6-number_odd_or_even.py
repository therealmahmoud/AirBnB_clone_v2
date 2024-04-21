#!/usr/bin/python3
""" A flask app. """
from flask import render_template
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


@HBNB.route('/python', strict_slashes=False)
@HBNB.route('/python/<text>', strict_slashes=False)
def display_python_user(text="is cool"):
    """ Displaying message of user."""
    text = text.replace('_', ' ')
    return "Python" + " " + text


@HBNB.route('/number/<int:n>', strict_slashes=False)
def display_n(n):
    if type(n) == int:
        return f"{n} is a number"
    else:
        return


@HBNB.route('/number_template/<int:n>', strict_slashes=False)
def display_html(n):
    return render_template('5-number.html', number=n)


@HBNB.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    return render_template('6-number_odd_or_even.html', number=n)

if __name__ == '__main__':
    HBNB.run(host="0.0.0.0", port=5000)
