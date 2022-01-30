#!/usr/bin/python3
"""Python is cool!"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """hello_route"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """hbnb"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """c_route"""
    return "C {}".format(text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """python is cool"""
    text = text.replace("_"," ")
    return "Python {}".format(text)


if __name__ == "__main__":
    app.run()
