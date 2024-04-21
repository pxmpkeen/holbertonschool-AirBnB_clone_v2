#!/usr/bin/python3
"""Flask"""

from flask import Flask, render_template
from models import storage, state


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    vals = storage.all(state.State)
    if id:
        return render_template("9-states.html", state=vals.get(f"State.{id}"))
    return render_template("7-states_list.html", vals=vals.values())


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
