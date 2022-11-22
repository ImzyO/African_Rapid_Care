#!/usr/bin/python3
"""module to define the views blueprint"""

from flask import Blueprint, render_template
from flask_login import login_required, current_user
import uuid
from models import database_storage

# create a blueprint
views = Blueprint('views', __name__)

# define route for home page
@views.route('/', strict_slashes=False)
# @login_required
def home():
    """go to home page"""
    return render_template('index.html', the_user=current_user,
                           cache_id=uuid.uuid4())

# define route for my appointments
@views.route('/appointments', strict_slashes=False)
@login_required
def appointments():
    """go to appointments page"""
    if the_user:
        # return all appointments for all users
        apt_objs = database_storage.all(Appointments).values()
        
    return render_template('appointments.html', the_user=current_user,
                           cache_id=uuid.uuid4(),
                           apt_objs=apt_objs)

@views.route('/book', strict_slashes=False)
@login_required
def book():
    """go to book appointment page"""
    return render_template('book.html', the_user=current_user,
                           cache_id=uuid.uuid4())

@views.route('/booking', strict_slashes=False)
@login_required
def booking():
    """go to booking appointment page"""
    return render_template('booking.html', the_user=current_user,
                           cache_id=uuid.uuid4())

@views.route('/store', strict_slashes=False)
@login_required
def store():
    """go to store page"""
    return render_template('store.html', the_user=current_user,
                           cache_id=uuid.uuid4())
