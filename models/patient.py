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
# from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


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


# class PatientSchema(SQLAlchemyAutoSchema):
#    """marshmallow schema"""
#    class Meta:
#       """class meta"""
#       model = Patient
#       load_instance = True
#       include_relationships = True
#       include_fk = True
