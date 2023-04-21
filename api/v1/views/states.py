#!/usr/bin/python3
"""
Create a new view for State objects that handles
all default RESTFul API actions:
"""
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from models import storage
from models.state import State
import models


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def status():
    slist = []
    states = storage.all(State).values()
    for state in states:
        slist.append(state.to_dict())
    return jsonify(slist)


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_state(state_id):
    """Retrieves a State object"""
    states = storage.all(State)
    key = "State."+state_id
    if key not in states:
        abort(404)
    a = states[key]
    return jsonify(a.to_dict())


@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_state(state_id):
    states = storage.all(State)
    key = "State."+state_id
    if key not in states:
        abort(404)
    a = states[key]
    storage.delete(a)
    storage.save()
    return jsonify({}), 200


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def post():
    js = request.get_json()
    if not js:
        abort(400, 'Not a JSON')
    if 'name' not in js:
        abort(400, 'Missing name')
    state = State(**js)
    storage.new(state)
    storage.save()
    return jsonify(state.to_dict()), 201


@app_views.route("/states/<state_id>", methods=["PUT"], strict_slashes=False)
def put(state_id):
    js = request.get_json()
    states = storage.all(State)
    key = "State."+state_id
    """Updates an object"""
    state_data = request.get_json()
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    elif not state_data:
        abort(400, "Not a JSON")
    a = states[key]
    m = a.__dict__
    for i in js:
        if i not in ["id", "created_at",
                     "updated_at"]:
            m[i] = js[i]
    storage.save()
    return jsonify(m.to_dict()), 200
