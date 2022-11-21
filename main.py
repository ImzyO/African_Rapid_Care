#!/usr/bin/python3
"""main file to launch the app"""

from web import create_app
from models import database_storage


app = create_app()

# begin flask page rendering
@app.teardown_appcontext
def teardown_db(exception):
    """
    after each request, this method calls .close() (i.e. .remove()) on
    the current SQLAlchemy Session
    """
    database_storage.close()

# only if we run the main.py file the app.run will execute
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
