#!/usr/bin/python3
"""module to define the views blueprint"""

from flask import Blueprint, render_template
from flask_login import login_required, current_user

# create a blueprint
views = Blueprint('views', __name__)

# define route for home page
@views.route('/', strict_slashes=False)
# @login_required
def home():
    """go to home page"""
    return render_template('index.html', the_user=current_user)

# define route for my appointments
@views.route('/appointments', strict_slashes=False)
@login_required
def appointments():
    """go to appointments page"""
    return render_template('appointments.html', the_user=current_user)

@views.route('/book', strict_slashes=False)
@login_required
def book():
    """go to book appointment page"""
    return render_template('book.html', the_user=current_user)

@views.route('/store', strict_slashes=False)
@login_required
def store():
    """go to store page"""
    return render_template('store.html', the_user=current_user)
