#!/usr/bin/python3
"""
Create a folder views inside v1
"""
import api.v1.views.index 
from flask import Blueprint

"""
Create a folder views inside v1
"""
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
