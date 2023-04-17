#!/usr/bin/python3
"""
mport app_views from api.v1.views
create a route /status on the object
app_views that returns a JSON: "status" ok
"""
from api.v1.views import app_views
from flask import Flask, jsonify
from models import storage
from models import amenity, city, place, review, state, user


@app_views.route('/status', strict_slashes=False)
def api_status():
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def count():
    a = {}
    a["amenities"] = storage.count(amenity.Amenity)
    a["cities"] = storage.count(city.City)
    a["places"] = storage.count(place.Place)
    a["reviews"] = storage.count(review.Review)
    a["states"] = storage.count(state.State)
    a["users"] = storage.count(user.User)
    return jsonify(a)
