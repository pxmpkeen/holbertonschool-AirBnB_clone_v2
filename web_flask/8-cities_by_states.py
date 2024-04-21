#!/usr/bin/python3
"""Flask inittin"""


from flask import Flask, render_template
from models import storage, state


app = Flask(__name__)


@app.route('/cities_by_states')
def cities_by_states():
    vals = storage.all(state.State).values()
    return render_template("8-cities_by_states.html", vals=vals)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)