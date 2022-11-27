#!/usr/bin/python3
"""module defines office associated with hospital and doctor"""


import models
import sqlalchemy
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Float
from sqlalchemy.orm import relationship
import requests
import json
# from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class Office(BaseModel, Base):
    """a class office associating doctor and hospital"""
    __tablename__ = "offices"

    longitude = Column(Float, nullable=False)
    latitude = Column(Float, nullable=False)
    country = Column(String(128), nullable=False)
    city = Column(String(128), nullable=False)
    office_address = Column(String(128), nullable=False)
    info = Column(String(1024), nullable=False)

    doctor_id = Column(String(60), ForeignKey('doctors.id'), nullable=False)
    hospital_id = Column(String(60),
                         ForeignKey('hospital_affiliation.id'),
                         nullable=False)

    office_hours = relationship('OfficeHours',
                                backref='office',
                                # cascade='delete'
                                cascade="all, delete, delete-orphan")
    appointments = relationship('Appointment',
                                backref='office',
                                # cascade='delete'
                                cascade="all, delete, delete-orphan")

    # one to many relationship between office and distance
    distances = relationship('Distance',
                             backref='office',
                             # cascade='delete',
                             cascade="all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        """initialization"""
        super().__init__(*args, **kwargs)

    """
    def __setattr__(self, name, value):
        # returns latitude and longitude of office locations on maps
        # requests.get(base_url, dictionary of{ APIKEY, address
        # of office}) converted to string using json
        url = 'https://maps.googleapis.com/maps/api/geocode/json?'
        APIKEY = 'AIzaSyCZaGxLDW9tX2gnOmqr2TEWo_UxJpVZtzI'
        location = requests.get(url,
                                {'API_KEY': APIKEY,
                                 'address': "office_address"}).json()
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
        """
