#!/usr/bin/python3
"""
Create a folder views inside v1
"""
from api.v1.views.index import *
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
