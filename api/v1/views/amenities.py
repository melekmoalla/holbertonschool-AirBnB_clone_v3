#!/usr/bin/python3
"""
Create a new view for State objects that handles
all default RESTFul API actions:
"""
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from models import storage
from models.amenity import Amenity
import models


@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
def status():
    slist = []
    states = storage.all(Amenity).values()
    for state in states:
        slist.append(state.to_dict())
    return jsonify(slist)


@app_views.route('/amenities/<amenity_id>', methods=['GET'], strict_slashes=False)
def get_state(amenity_id):
    """Retrieves a State object"""
    states = storage.all(Amenity)
    key = "Amenity."+amenity_id
    if key not in states:
        abort(404)
    a = states[key]
    return jsonify(a.to_dict())


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_state(amenity_id):
    states = storage.all(Amenity)
    key = "Amenity."+amenity_id
    if key not in states:
        abort(404)
    a = states[key]
    storage.delete(a)
    storage.save()
    return jsonify({}), 200


@app_views.route('/amenities', methods=['POST'], strict_slashes=False)
def post():
    js = request.get_json()
    if not js:
        abort(400, 'Not a JSON')
    if 'name' not in js:
        abort(400, 'Missing name')
    state = Amenity(**js)
    storage.new(state)
    storage.save()
    return jsonify(state.to_dict()), 201


@app_views.route('/amenities/<amenity_id>', methods=['PUT'], strict_slashes=False)
def put(amenity_id):
    states = storage.all(Amenity)
    key = "Amenity."+amenity_id
    if key not in states:
        abort(404)
    js = request.get_json()
    if not js:
        abort(400, 'Not a JSON')
    a = states[key]
    m = a.__dict__
    for i in js:
        if i not in ["id", "created_at",
                     "updated_at"]:
            m[i] = js[i]
    storage.save()
    return jsonify(m.to_dict()), 200
