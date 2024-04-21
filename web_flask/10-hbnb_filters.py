#!/usr/bin/python3
"""flask"""

from flask import Flask, render_template
from models import storage, state, amenity


app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    states = storage.all(state.State).values()
    amenities = storage.all(amenity.Amenity).values()
    return render_template("10-hbnb_filters.html", states=states, amenites=amenities)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)