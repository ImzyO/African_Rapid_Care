#!/usr/bin/python3
"""main file to launch the app"""

from web import create_app


app = create_app()
# only if we run the main.py file the app.run will execute
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
