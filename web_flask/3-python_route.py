#!/usr/bin/python3
"""hello flask"""


from flask import Flask

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)