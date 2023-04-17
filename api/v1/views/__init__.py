#!/usr/bin/python3
"""
Create a folder views inside v1
"""
from flask import Blueprint
import api
from api.v1.views.index import *

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')  