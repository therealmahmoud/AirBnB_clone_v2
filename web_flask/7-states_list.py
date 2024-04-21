#!/usr/bin/python3
""" Starts a Flask web application. """
import models
from flask import Flask
from flask import render_template

HBNB = Flask(__name__)


@HBNB.route("/states_list", strict_slashes=False)
def states_list():
    """Displays an HTML page with a list of all State objects in DBStorage.

    States are sorted by name.
    """
    states = models.storage.all("State")
    return render_template("7-states_list.html", states=states)


@HBNB.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    models.storage.close()


if __name__ == "__main__":
    HBNB.run(host="0.0.0.0")
