#!/usr/bin/python3
"""Write a script that starts a Flask web application and returns greetings"""
from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def Hello_HBNB():
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def HBNB():
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    # Replace underscores with spaces in the text
    text = text.replace("_", " ")
    return "C {}".format(python_text)

@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text):
    text = text.replace("_", " ")
    return "Python {}".format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
