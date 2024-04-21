#!/usr/bin/python3
"""Initting Flask"""

from flask import Flask, render_template
from models import storage, state


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    vals = storage.all(state.State).values()
    return render_template("7-states_list.html", vals=vals)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
