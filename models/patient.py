#!/usr/bin/python3
"""module defines a class Patient"""


import models
import sqlalchemy
from models.user import User
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy import DateTime
from sqlalchemy.orm import relationship


class Patient(User):
    """patient class with attributes of patient"""

    __tablename__ = "patients"
    id = Column(String(60),
                ForeignKey("users.id"),
                primary_key=True,
                nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    country = Column(String(100), nullable=False)
    city = Column(String(100), nullable=False)
    address = Column(String(200), nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'patient',
    }

    # one to many relationship between patients and appointments
    appointments = relationship('Appointment',
                                backref='patient',
                                cascade="all, delete, delete-orphan")

    # one to many relationship between patient and review
    reviews = relationship('Review',
                           backref='patient',
                           cascade="all, delete, delete-orphan")

    # one to many relationship between patient and distance
    distances = relationship('Distance',
                             backref='patient',
                             cascade="all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        """initialization"""
        super().__init__(*args, **kwargs)

    """
    def __setattr__(self, name, value):
        # sets password, latitude and longitude attributes
        if name == "password":
            value = hashlib.sha512(value.encode()).hexdigest()
            g = geocoder.ip('me')
            gcode = g.latlng
        if name == "latitude":
            value = g.latlng[0]
            value = 1.656898
        if name == "longitude":
            value = g.latlng[1]
            value = 1.65987
        super().__setattr__(name, value)
    """
