#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Doctor - Specialization """
from models.place import Doctor
from models.amenity import Specialization
from models import database_storage
from api.v1.views import app_views
import os
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('doctors/<doctor_id>/specializations', methods=['GET'],
                 strict_slashes=False)
@swag_from('documentation/doctor_specialization/get_doctors_specializations.yml',
           methods=['GET'])
def get_doctors_specializations(doctor_id):
    """Retrieves the list of all Specialization objects of a Doctor"""
    doctor = database_storage.get(Doctor, doctor_id)

    if not doctor:
        abort(404)

    if environ.get('ARC_MYSQL_DB') == "db":
        specializations = [specialization.to_dict() for specialization in doctor.specializations]

    return jsonify(specializations)


@app_views.route('/doctors/<doctor_id>/specializations/<specialization_id>',
                 methods=['DELETE'], strict_slashes=False)
@swag_from('documentation/doctor_specialization/delete_doctor_specializations.yml',
           methods=['DELETE'])
def delete_doctor_specialization(doctor_id, specialization_id):
    """Deletes a Specialization object of a Doctor"""
    doctor = database_storage.get(Doctor, doctor_id)

    if not doctor:
        abort(404)

    specialization = database_storage.get(Specialization, specialization_id)

    if not specialization:
        abort(404)

    if environ.get('ARC_MYSQL_DB') == "db":
        if specialization not in doctor.specializations:
            abort(404)
        doctor.specializations.remove(specialization)

    database_storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/doctors/<doctor_id>/specializations/<specialization_id>', methods=['POST'],
                 strict_slashes=False)
@swag_from('documentation/doctor_specialization/post_doctor_specializations.yml',
           methods=['POST'])
def post_doctor_specialization(doctor_id, specialization_id):
    """Link a Specialization object to a Doctor"""
    doctor = database_storage.get(Doctor, doctor_id)

    if not doctor:
        abort(404)

    specialization = database_storage.get(Specialization, specialization_id)

    if not specialization:
        abort(404)

    if environ.get('ARC_MYSQL_DB') == "db":
        if specialization in doctor.specializations:
            return make_response(jsonify(specialization.to_dict()), 200)
        else:
            doctor.specializations.append(specialization)

    database_storage.save()
    return make_response(jsonify(specialization.to_dict()), 201)
