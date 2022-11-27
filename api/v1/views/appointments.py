#!/usr/bin/python3
"""
a new view for appointment objects that handles
all default RESTFul API actions:
"""
from flask import jsonify, abort, make_response, request
from models import database_storage
from models.appointment import Appointment
from api.v1.views import app_views
from models.patient import Patient
from models.doctor import Doctor
from models.office import Office
from models.appointment_status import AppointmentStatus
# from flasgger.utils import swag_from


@app_views.route('/appointments',
                 methods=['GET'],
                 strict_slashes=False)
# @swag_from('documentation/appointment/get_appointment.yml',
#           methods=['GET'])
def get_appointments():
    """
    Retrieves the list of all appointment objects
    note; to_dict method is customised(class name, id,
    created & updated at)
    """
    all_appointments = database_storage.all(Appointment).values()
    list_appointments = []
    for appointment in all_appointments:
        list_appointments.append(appointment.to_dict())
    return jsonify(list_appointments)


@app_views.route('/appointments/<appointment_id>',
                 methods=['GET'],
                 strict_slashes=False)
# @swag_from('documentation/appointment/get_id_appointment.yml',
#           methods=['get'])
def get_appointment(appointment_id):
    """ Retrieves a specific appointment object """
    appointment = database_storage.get_byID(Appointment, appointment_id)
    if not appointment:
        abort(404)

    return jsonify(appointment.to_dict())


@app_views.route('/appointments/<appointment_id>',
                 methods=['DELETE'],
                 strict_slashes=False)
# @swag_from('documentation/appointment/delete_appointment.yml',
#           methods=['DELETE'])
def delete_appointment(appointment_id):
    """Deletes a appointment Object"""

    appointment = database_storage.get(Appointment, appointment_id)

    if not appointment:
        abort(404)

    database_storage.delete(appointment)
    database_storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/appointments',
                 methods=['POST'],
                 strict_slashes=False)
# @swag_from('documentation/appointment/post_appointment.yml',
#           methods=['POST'])
def post_appointment():
    """Creates a appointment"""
    if not request.get_json():
        abort(400, description="Not a JSON")

    details = ["start_time", "end_time", "symptoms",
               "appointment_type"]
    for detail in details:
        if detail not in request.get_json():
            abort(400, description="Missing" + detail)

    data = request.get_json()
    appointment = appointment(**data)
    appointment.save()
    return make_response(jsonify(appointment.to_dict()), 201)


@app_views.route('/appointments/<appointment_id>',
                 methods=['PUT'],
                 strict_slashes=False)
# @swag_from('documentation/appointment/put_appointment.yml',
#           methods=['PUT'])
def put_appointment(appointment_id):
    """Updates a appointment"""
    appointment = database_storage.get_byID(Appointment, appointment_id)

    if not appointment:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(appointment, key, value)
    database_storage.save()
    return make_response(jsonify(appointment.to_dict()), 200)
