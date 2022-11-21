#!/usr/bin/python3
"""
a new view for Specialization objects that handles
all default RESTFul API actions:
"""
from flask import jsonify, abort, make_response, request
from models import database_storage
from models.user import Specialization
from api.v1.views import app_views
from flasgger.utils import swag_from


@app_views.route('/specializations', methods=['GET'], strict_slashes=False)
@swag_from('documentation/specialization/get_specialization.yml', methods=['GET'])
def get_specializations():
    """
    Retrieves the list of all Specialization objects
    note; to_dict method is customised(class name, id,
    created & updated at)
    """
    all_specializations = database_storage.all(Specialization).values()
    list_specializations = []
    for specialization in all_specializations:
        list_specializations.append(specializations.to_dict())
    return jsonify(list_specializations)


@app_views.route('/specializations/<specialization_id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/specialization/get_id_specialization.yml', methods=['get'])
def get_specialization(specialization_id):
    """ Retrieves a specific Specialization object """
    specialization = database_storage.get(Specialization, specialization_id)
    if not specialization:
        abort(404)

    return jsonify(specialization.to_dict())


@app_views.route('/specializations/<specialization_id>', methods=['DELETE'],
                 strict_slashes=False)
@swag_from('documentation/specialization/delete_specialization.yml', methods=['DELETE'])
def delete_specialization(specialization_id):
    """Deletes a Specialization Object"""

    specialization = storage.get(Specialization, specialization_id)

    if not specialization:
        abort(404)

    database_storage.delete(specialization)
    database_storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/specializations', methods=['POST'], strict_slashes=False)
@swag_from('documentation/specialization/post_specialization.yml', methods=['POST'])
def post_specialization():
    """Creates a Specialization"""
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'name' not in request.get_json():
        abort(400, description="Missing name")

    data = request.get_json()
    instance = Specialization(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/specializations/<specialization_id>', methods=['PUT'], strict_slashes=False)
@swag_from('documentation/specialization/put_specialization.yml', methods=['PUT'])
def put_specialization(specialization_id):
    """Updates a Specialization"""
    specialization = database_storage.get(Specialization, specialization_id)

    if not specialization:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(state, key, value)
    database_storage.save()
    return make_response(jsonify(specialization.to_dict()), 200)
