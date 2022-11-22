#!/usr/bin/python3
"""module defines a class Patient"""


import models
import sqlalchemy
from models.user import User
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy import DateTime
from sqlalchemy.orm import relationship
import geocoder
# import hashlib


class Patient(User):
    """patient class with attributes of patient"""

    __tablename__ = "patients"
    id = Column(String(60),
                ForeignKey("users.id"),
                primary_key=True,
                nullable=False)
    # user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    country = Column(String(100), nullable=False)
    city = Column(String(100), nullable=False)
    address = Column(String(200), nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'patient',
    }

    # attributes from user
    # user_name = Column(String(100), nullable=False)
    # email = Column(String(100), unique=True, nullable=False)
    # password = Column(String(200), nullable=False)
    # phone_number = Column(String(100), nullable=False)
    # first_name = Column(String(100), nullable=False)
    # last_name = Column(String(100), nullable=False)
    # gender = Column(String(100), nullable=False)
    # birthdate = Column(DateTime, nullable=False)

    # one to many relationship between patients and appointments
    appointments = relationship('Appointment',
                                backref='patient',
                                # primaryjoin="Appointment.patient_id==Patient.id",
                                # cascade='delete'
                                # add cascade
                                cascade="all, delete, delete-orphan")

    # one to many relationship between patient and review
    reviews = relationship('Review',
                           backref='patient',
                           # cascade='delete',
                           cascade="all, delete, delete-orphan")

    # one to many relationship between patient and distance
    distances = relationship('Distance',
                             backref='patient',
                             # cascade='delete',
                             cascade="all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        """initialization"""
        super().__init__(*args, **kwargs)

    # def __setattr__(self, name, value):
    #    """sets password, latitude and longitude attributes"""
        # if name == "password":
        #    value = hashlib.sha512(value.encode()).hexdigest()
        # g = geocoder.ip('me')
        # gcode = g.latlng
    #    if name == "latitude":
    #         value = g.latlng[0]
    #        value = 1.656898
    #    if name == "longitude":
    #         value = g.latlng[1]
    #        value = 1.65987
    #    super().__setattr__(name, value)

     def __setattr__(self, name, value):
        """returns latitude and longitude of patient locations on maps"""
        # requests.get(base_url, dictionary of{ APIKEY, address
        # of office}) converted to string using json
        url = 'https://maps.googleapis.com/maps/api/geocode/json?'
        APIKEY = 'AIzaSyCZaGxLDW9tX2gnOmqr2TEWo_UxJpVZtzI' # need to change api key because this one is used by office
        location = requests.get(url,
                                {'API_KEY': APIKEY,
                                 'address': "address"}).json()
        location.keys()

        # loaction.keys returns dict of keys['results, 'status]
        if location['status'] == "OK":

            # note the key results contains a dictionary of address
            # components:city/locality/long name/geometry-lat&long
            # since we need the exact location, we use the geometry
            # key which returns a dictionary,
            # containing bounds/location/northeast/southeast etc lat and long

            geometry = location['result'][0]['geometry']
            if name == 'latitude':
                value = float(geometry['location']['lat'])
            if name == 'longitude':
                value = float(geometry['location']['long'])

        super().__setattr__(name, value)
