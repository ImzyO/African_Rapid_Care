#!/usr/bin/python3
"""
a new view for Doctor objects that handles
all default RESTFul API actions:
"""
from flask import jsonify, abort, make_response, request
from models import database_storage
from models.doctor import Doctor
from api.v1.views import app_views
# from flasgger.utils import swag_from


@app_views.route('/doctors',
                 methods=['GET'],
                 strict_slashes=False)
# @swag_from('documentation/doctor/get_doctor.yml',
#           methods=['GET'])
def get_doctors():
    """
    Retrieves the list of all Doctor objects
    note; to_dict method is customised(class name, id,
    created & updated at)
    """
    all_doctors = database_storage.all(Doctor).values()
    list_doctors = []
    for doctor in all_doctors:
        list_doctors.append(doctor.to_dict())
    return jsonify(list_doctors)


@app_views.route('/doctors/<doctor_id>',
                 methods=['GET'],
                 strict_slashes=False)
# @swag_from('documentation/doctor/get_id_doctor.yml',
#           methods=['get'])
def get_doctor(doctor_id):
    """ Retrieves a specific Doctor object """
    doctor = database_storage.get_byID(Doctor, doctor_id)
    if not doctor:
        abort(404)

    return jsonify(doctor.to_dict())


@app_views.route('/doctors/<doctor_id>',
                 methods=['DELETE'],
                 strict_slashes=False)
# @swag_from('documentation/doctor/delete_doctor.yml',
#           methods=['DELETE'])
def delete_doctor(doctor_id):
    """Deletes a Doctor Object"""

    doctor = storage.get_byID(Doctor, doctor_id)

    if not doctor:
        abort(404)

    database_storage.delete(doctor)
    database_storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/doctors',
                 methods=['POST'],
                 strict_slashes=False)
# @swag_from('documentation/doctor/post_doctor.yml',
#           methods=['POST'])
def post_doctor():
    """Creates a Doctor"""
    if not request.get_json():
        abort(400, description="Not a JSON")

    details = ["user_name", "email", "password",
               "first_name", "last_name", "gender",
               "phone_number", "birthdate"]
    for detail in details:
        if detail not in request.get_json():
            abort(400, description="Missing" + detail)

    data = request.get_json()
    doctor = Doctor(**data)
    doctor.save()
    return make_response(jsonify(doctor.to_dict()), 201)


@app_views.route('/doctors/<doctor_id>',
                 methods=['PUT'],
                 strict_slashes=False)
# @swag_from('documentation/doctor/put_doctor.yml',
#           methods=['PUT'])
def put_doctor(doctor_id):
    """Updates a Doctor"""
    doctor = database_storage.get_byID(Doctor, doctor_id)

    if not doctor:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(doctor, key, value)
    database_storage.save()
    return make_response(jsonify(doctor.to_dict()), 200)
