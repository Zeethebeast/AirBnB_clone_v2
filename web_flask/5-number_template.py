#!/usr/bin/python3
"""Write a script that starts a Flask web application and returns greetings"""
from flask import Flask, render_template

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
    text = text.replace('_', ' ')
    return "C {}".format(text)

@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text):
    text = text.replace('_', ' ')
    return "Python {}".format(text)

@app.route("/number/<int:n>", strict_slashes=False)
def number_n(n):
    if n > 0:
        return "{} is a number".format(n)
    return 

@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    if n > 0:
        return render_template('5-number.html', number=n)
    return 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
