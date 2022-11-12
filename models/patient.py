#!/usr/bin/python3
"""module defines a class Patient"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.orm import relationship
import geocoder


class Patient(User):
    """patient class with attributes of patient"""

    __tablename = "patients"
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    country = Column(String(100), nullable=False)
    city = Column(String(100), nullable=False)
    address = Column(String(200), nullable=False)
    
    # one to many relationship between patients and appointments
    appointments = relationship('Appointment', backref='patient', cascade='delete')
    
    # one to many relationship between patient and review
    reviews = relationship('Review', backref='patient', cascade='delete')

    g = geocoder.ip('me')
    gcode = g.latlng

    def __init__(self, *args, **kwargs):
        """initialization"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """sets latitude and longitude attributes"""
        if name == "latitude":
            value = g.latlng[0]
        if name == "longitude":
            value = g.latlng[1]
        super().__setattr__(name, value)
