#!/usr/bin/python3
"""module to define the auth blueprint"""

from flask import Blueprint, render_template
from flask import request, flash, redirect, url_for
from models import user
User = user.User
from models import patient
Patient = patient.Patient
from models import office
Office = office.Office
from models.distance import Distance
from models import database_storage
import uuid
# import geocoder
from flask_login import login_user, login_required
from flask_login import logout_user, current_user
import hashlib


# create a blueprint
auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def login():
    """got to login page"""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        the_user = database_storage.session.query(User).filter_by(email=email).first()
        if the_user:
            if the_user.password == hashlib.sha512(password.encode()).hexdigest():
                flash("Logged in successfully!", category="success")
                login_user(the_user, remember=True)
                return redirect(url_for('views.appointments'))
            else:
                flash("Incorrect password!", category="error")
        else:
            flash("Email doesn't exist.", category="error")
    return render_template('login.html', the_user=current_user,
                           cache_id=uuid.uuid4())

@auth.route('/logout', strict_slashes=False)
@login_required 
def logout():
    """Logout only accessible when user is logged in"""
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'],
            strict_slashes=False)
def sign_up():
    """got to sign-up page"""
    if request.method == "POST":
        user_name = request.form.get('user_name')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        birthdate = request.form.get('birthdate')
        gender = request.form.get('gender')
        phone_number = request.form.get('phone_number')
        country = request.form.get('country')
        city = request.form.get('city')
        address = request.form.get('address')
        # g = geocoder.ip('me')
        # gcode = g.latlng
        # latitude = g.latlng[0]
        # longitude = g.latlng[1]
        latitude = 0.000
        longitude = 0.000

        the_user = database_storage.session.query(User).filter_by(email=email).first()
        if the_user:
            flash("User already exists.", category="error")
        elif len(email) < 5:
            flash("Email must have more characters!", category='error')
        elif len(first_name) < 2:
            flash("First Name must have more characters!", category='error')
        elif len(last_name) < 2:
            flash("Last Name must have more characters!", category='error')
        elif password1 != password2:
            flash("Your passwords don't match!", category='error')
        elif len(password1) < 7:
            flash("Password must have more characters!", category='error')
        elif len(address) < 10:
            flash("Address must have more characters!", category='error')
        else:
            # new_user = user.User(user_name=user_name, email=email,
            #                     password=password1, first_name=first_name,
            #                     last_name=last_name, birthdate=birthdate,
            #                     gender=gender, phone_number=phone_number,
            #                     country=country, city=city,
            #                     address=address)
            the_user = Patient()
            the_user.user_name = user_name
            the_user.email = email
            the_user.password = password1
            the_user.first_name = first_name
            the_user.last_name = last_name
            the_user.birthdate = birthdate
            the_user.gender = gender
            the_user.phone_number = phone_number
            the_user.country = country
            the_user.city = city
            the_user.address = address
            the_user.latitude = latitude
            the_user.longitude = longitude
            the_user.save()
            # Create entries in the distances table
            offices = database_storage.all(Office).values()   
            for office in offices:
                distance_entry = Distance()
                distance_entry.patient_id = the_user.id
                distance_entry.office_id = office.id
                distance_entry.distance_text="0 km"
                distance_entry.distance = 0000
                distance_entry.save()
            # add creation of that user as patient
            login_user(the_user, remember=True) 
            flash("Account created!", category='success')
            return redirect(url_for('views.appointments'))

    return render_template('sign-up.html', the_user=current_user,
                           cache_id=uuid.uuid4())

@auth.route('/settings', strict_slashes=False)
@login_required
def settings():
    """got to settings page"""
    return render_template('settings.html', the_user=current_user,
                           cache_id=uuid.uuid4())

@auth.route('/account',
            methods=['GET', 'POST'],
            strict_slashes=False)
@login_required
def account():
    """got to account page"""
    count = 0
    the_user = database_storage.get_byID(User, current_user.id)
    patient = database_storage.get_byID(Patient, current_user.id)
    if request.method == "POST":
        email = request.form.get('email')
        previous_password = request.form.get('previous_password')
        new_password = request.form.get('new_password')
        new_password2 = request.form.get('new_password2')
        city = request.form.get('city')
        address = request.form.get('address')
        
        if email != the_user.email:
            if len(email) < 5:
                    flash("Email must have more characters!", category='error')
            else:
                database_storage.session.query(User).filter(
                    User.id == the_user.id).update(
                        {User.email: email})
                database_storage.save()
                count +=1

        if previous_password:
            verify_pwd = hashlib.sha512(previous_password.encode()).hexdigest()
            if verify_pwd != the_user.password:
                flash("Previous password incorrect!", category='error')
            else:
                if new_password != new_password2:
                    flash("Your passwords don't match!", category='error')
                elif len(new_password) < 7:
                    flash("Password must have more characters!", category='error')
                else:
                    database_storage.session.query(User).filter(
                        User.id == the_user.id).update(
                            {User.password: hashlib.sha512(new_password.encode()).hexdigest()})
                    database_storage.save()
                    count +=1
                    # logout_user()
                    # return redirect(url_for('auth.login'))
        
        if city != patient.city:
            database_storage.session.query(Patient).filter(
                            Patient.id == the_user.id).update(
                                {Patient.city: city})
            database_storage.save()
            count +=1

        if address != patient.address:
            if len(address) < 10:
                flash("Address must have more characters!", category='error')
            else:
                database_storage.session.query(Patient).filter(
                            Patient.id == the_user.id).update(
                                {Patient.address: address})
                database_storage.save()
                count +=1
        
        if count > 0:
            flash("Changes saved!", category='success')

    return render_template('account.html',
    #                       account=account,
                           the_user=current_user,
                           cache_id=uuid.uuid4())
