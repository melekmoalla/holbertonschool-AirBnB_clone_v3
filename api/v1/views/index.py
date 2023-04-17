#!/usr/bin/python3
"""
mport app_views from api.v1.views
create a route /status on the object
app_views that returns a JSON: "status" ok
"""
from api.v1.views import app_views
from flask import Flask, jsonify
import models.engine
from models import amenity, city, place, review, state, user


@app_views.route('/status', strict_slashes=False)
def api_status():
    return jsonify({"status": "OK"})


@app_views.route('/api/v1/stats', strict_slashes=False)
def count():
    a = {}
    a["amenities"] = count(amenity.Amenity)
    a["cities"] = count(city.City)
    a["places"] = count(place.Place)
    a["reviews"] = count(review.Review)
    a["states"] = count(state.State)
    a["users"] = count(user.User)
    return jsonify(a)
