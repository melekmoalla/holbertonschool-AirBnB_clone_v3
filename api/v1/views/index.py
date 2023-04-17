#!/usr/bin/python3
"""
mport app_views from api.v1.views
create a route /status on the object
app_views that returns a JSON: "status" ok
"""
from api.v1.views import app_views
from flask import Flask, jsonify

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def api_status():
    return jsonify(status="OK")
