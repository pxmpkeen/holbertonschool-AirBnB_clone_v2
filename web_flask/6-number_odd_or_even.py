#!/usr/bin/python3
"""hello flask"""


from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello():
        return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
      return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c(text):
      changed_var = text.replace("_", " ")
      return changed_var

@app.route("/python/<text>", strict_slashes=False)
def python(text):
      changed_word = text.replace("_", " ")
      return f"Python {changed_word}"

@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    return f"{n} is a number"

@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
      return render_template('5-number.html', n=n)

@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_type(n):
      return render_template('6-number_odd_or_even.html', n=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)