#!/usr/bin/python3
"""Flask application"""

from flask import Flask, jsonify, make_response
from models import database_storage
from api.v1.views import app_views
from flask_cors import CORS
from flasgger import Swagger
from flasgger.utils import swag_from
from os import environ
# from flask_marshmallow import Marshmallow


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
# cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
# app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_database(error):
    """ Close database_storage """
    database_storage.close()

@app.errorhandler(404)
def not_found(error):
    """a handler for 404 errors that returns a
    JSON-formatted 404 status code response"""

    return make_response(jsonify({'error': "Not found"}), 404)

app.config['SWAGGER'] = {
    'title': 'African Rapid Care Restful API',
    'uiversion': 3
}

Swagger(app)

# ma = Marshmallow(app)


if __name__ == "__main__":
    host = environ.get("ARC_API_HOST")
    port = environ.get("ARC_API_PORT")

    if not host:
        host = "0.0.0.0"
    if not port:
        port ="5001"
    app.run(host=host, port=port, threaded=True)
