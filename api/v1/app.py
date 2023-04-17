#!/usr/bin/python3
"""
create a variable app, instance of Flask
"""

from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
import os

app = Flask(__name__)
app.register_blueprint(app_views)


@app.route("/")
def hello():
    return ("mayouka")


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()

"""
create a handler for 404 errors that
returns a JSON-formatted 404 status code
response
"""
@app.error_processor
def my_error_processor(error):
    return jsonify({"error": "Not found"})


if __name__ == "__main__":
    host = os.getenv("HBNB_API_HOST", "0.0.0.0")
    port = os.getenv("HBNB_API_PORT", 5000)
    app.run(host=host, port=port, threaded=True)
