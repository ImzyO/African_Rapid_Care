#!/usr/bin/python3
"""__init__ module to create the app"""
from flask import Flask
from models import database_storage
from models import user
from models import patient
from models import doctor
from models import review
from models import specialization
from models import appointment
Appointment = appointment.Appointment
from models import appointment_status
from models import hospital_affiliation
from models import office
from models import office_hours
import os
from dotenv import load_dotenv
from flask_login import LoginManager
User = user.User


load_dotenv()


def create_app():
    """create a flask application"""
    app = Flask(__name__)
    # encrypt/secure cookies and session data
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    # register our views
    from .views import views
    from .auth import auth
    from .footer_views import footer_views

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(footer_views, url_prefix='/')

    # we create and initialize the Flask login extension
    login_manager = LoginManager()
    # go to login view if we are not logged in
    login_manager.login_view = 'auth.login'
    # link login_manager instance to the app
    login_manager.init_app(app)

    # telling flask how we load a user
    @login_manager.user_loader
    def load_user(id):
        """
        Function that links database with Flask storing
        the user_ID in a session
        """ 
        # return User.query.get(int(id))
        return database_storage.session.query(User).get(id)

    return app
