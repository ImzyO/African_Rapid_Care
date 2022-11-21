#!/usr/bin/python3
"""Flask application"""

from flask import Flask, jsonify, make_response
from models import database_storage
from api.v1.views import app_views
import os


app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def close_database(error):
    """ Close database_storage """
    database_storage.close()

@app.errorhandler(404)
def not_found(error):
    """a handler for 404 errors that returns a
    JSON-formatted 404 status code response"""

    return make_response(jsonify({'error': "Not found"}), 404)

if __name__ == "__main__":
    host = environ.get("ARC_MYSQL_HOST")
    port = environ.get("ARC_MYSQL_PORT")

    if not host:
        host = "0.0.0.0"
    if not port:
        port ="5000"
    app.run(host=host, port=port, threaded=True)
