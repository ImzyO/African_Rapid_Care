#!/usr/bin/python3
"""
a new view for Patient objects that handles
all default RESTFul API actions:
"""
from flask import jsonify, abort, make_response, request
from models import database_storage
from models.user import Patient
from api.v1.views import app_views
# from flasgger.utils import swag_from


@app_views.route('/patients', methods=['GET'], strict_slashes=False)
# @swag_from('documentation/patient/get_patient.yml', methods=['GET'])
def get_patients():
    """
    Retrieves the list of all Patient objects
    note; to_dict method is customised(class name, id,
    created & updated at)
    """
    all_patients = database_storage.all(Patient).values()
    list_patients = []
    for patient in all_patients:
        list_patients.append(patient.to_dict())
    return jsonify(list_patients)


@app_views.route('/patients/<patient_id>', methods=['GET'], strict_slashes=False)
# @swag_from('documentation/patient/get_id_patient.yml', methods=['get'])
def get_patient(patient_id):
    """ Retrieves a specific Patient object """
    patient = database_storage.get(Patient, patient_id)
    if not patient:
        abort(404)

    return jsonify(patient.to_dict())


@app_views.route('/patients/<patient_id>', methods=['DELETE'],
                 strict_slashes=False)
# @swag_from('documentation/patient/delete_patient.yml', methods=['DELETE'])
def delete_user(patient_id):
    """Deletes a Patient Object"""

    patient = storage.get(Patient, patient_id)

    if not patient:
        abort(404)

    database_storage.delete(patient)
    database_storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/patients', methods=['POST'], strict_slashes=False)
# @swag_from('documentation/patient/post_patient.yml', methods=['POST'])
def post_patient():
    """Creates a Patient"""
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'name' not in request.get_json():
        abort(400, description="Missing name")

    data = request.get_json()
    instance = Patient(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/patients/<patient_id>', methods=['PUT'], strict_slashes=False)
# @swag_from('documentation/patient/put_patient.yml', methods=['PUT'])
def put_patient(patient_id):
    """Updates a Patient"""
    patient = database_storage.get(Patient, patient_id)

    if not patient:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(state, key, value)
    database_storage.save()
    return make_response(jsonify(patient.to_dict()), 200)
