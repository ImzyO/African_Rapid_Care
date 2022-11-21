#!/usr/bin/python3
"""API Blueprint"""

from flask import Blueprint
from api.v1.views.index import *
from api.v1.views.users import *
from api.v1.views.patients import *
from api.v1.views.doctors import *

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

