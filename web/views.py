#!/usr/bin/python3
"""module to define the views blueprint"""

from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from flask import flash, redirect, url_for
import uuid
from models import database_storage
from models import appointment
Appointment = appointment.Appointment
from models import doctor
Doctor = doctor.Doctor
from models import distance
Distance = distance.Distance
from models import office_hours
OfficeHours = office_hours.OfficeHours
from datetime import datetime
from sqlalchemy import update


# create a blueprint
views = Blueprint('views', __name__)

# define route for home page
@views.route('/', strict_slashes=False)
# @login_required
def home():
    """go to home page"""
    the_user = current_user
    return render_template('index.html', the_user=current_user,
                           cache_id=uuid.uuid4())

# define route for my appointments
@views.route('/appointments', strict_slashes=False)
@login_required
def appointments():
    """go to appointments page"""
    the_user = current_user
    if the_user:
        apt_objs = database_storage.all(Appointment).values()
        doctors = database_storage.all(Doctor).values()
        distances = database_storage.all(Distance).values()
        
    return render_template('appointments.html', the_user=current_user,
                           cache_id=uuid.uuid4(),
                           apt_objs=apt_objs,
                           doctors=doctors,
                           distances=distances)

@views.route('/book', strict_slashes=False)
@login_required
def book():
    """go to book appointment page"""
    the_user = current_user
    if the_user:

        oh_objs = database_storage.all(OfficeHours).values()

        doctors = database_storage.all(Doctor).values()
        distances = database_storage.all(Distance).values()
    return render_template('book.html', the_user=current_user,
                           cache_id=uuid.uuid4(),
                           oh_objs=oh_objs)

@views.route('/booking',
             methods=['GET', 'POST'],
             strict_slashes=False)
@login_required
def booking():
    """go to booking appointment page"""
    time = "%a, %d %b %Y %H:%M:%S %Z"
    if request.method == "POST":
        patient_id = request.form.get('patient_id')
        day_of_the_week = request.form.get('day_of_the_week')
        office_id = request.form.get('office_id')
        start_time = datetime.strptime(request.form.get('start_time'), time)
        end_time = datetime.strptime(request.form.get('start_time'), time)
        appointment_status_id = request.form.get('appointment_status_id')
        symptoms = request.form.get('symptoms')
        office_hour_id = request.form.get('office_hour_id')

        appointment_booked = Appointment()
        appointment_booked.patient_id = patient_id
        appointment_booked.office_id = office_id
        appointment_booked.day_of_the_week = day_of_the_week
        appointment_booked.start_time = start_time
        appointment_booked.end_time = end_time
        
        appointment_booked.appointment_type = "Physical"
        appointment_booked.appointment_status_id = "730a8a28-83f3-422c-9435-ee4327c2b0b7"
        appointment_booked.symptoms = symptoms
        appointment_booked.save()

        # mark the slot as not available
        database_storage.session.query(OfficeHours).filter(
            OfficeHours.id == office_hour_id).update(
                {OfficeHours.availability: "No"})
        database_storage.save()
        flash("Appointment Booked!", category='success')
        return redirect(url_for('views.appointments'))

    return render_template('booking.html', the_user=current_user,
                           cache_id=uuid.uuid4())

@views.route('/store', strict_slashes=False)
@login_required
def store():
    """go to store page"""
    return render_template('store.html', the_user=current_user,
                           cache_id=uuid.uuid4())
