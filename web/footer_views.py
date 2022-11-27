#!/usr/bin/python3
"""module to define the footer_views blueprint"""

from flask import Blueprint, render_template
from flask_login import login_required, current_user
import uuid
from flask import request, flash, redirect, url_for


# create a blueprint
footer_views = Blueprint('footer_views', __name__)

# define route for about page
@footer_views.route('/about', strict_slashes=False)
def about():
    """go to about page"""
    return render_template('about.html', the_user=current_user,
                           cache_id=uuid.uuid4())

# define route for contact page
@footer_views.route('/contact',
                    methods=['GET', 'POST'],
                    strict_slashes=False)
def contact():
    """go to contact page"""
    if request.method == "POST":
        flash("Thank you for your message, we'll come back to you shortly!", category="success")
        return redirect(url_for('views.home'))
    return render_template('contact.html', the_user=current_user,
                           cache_id=uuid.uuid4())

@footer_views.route('/help', strict_slashes=False)
def help():
    """go to help page"""
    return render_template('help.html', the_user=current_user,
                           cache_id=uuid.uuid4())

@footer_views.route('/terms-privacy', strict_slashes=False)
def terms_privacy():
    """go to terms-privacy page"""
    return render_template('terms-privacy.html', the_user=current_user,
                           cache_id=uuid.uuid4())
