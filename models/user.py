#!/usr/bin/python3
"""
module defines a class user: who could be a patient/doctor:
attributes apply to both as they are both users
"""


import models
import sqlalchemy
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship
import hashlib
from flask_login import UserMixin
# from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
# from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
# from marshmallow import Schema, fields

class User(BaseModel, Base, UserMixin):
    """user class with attributes of user"""
    """user relates to doctor and patient modules via Foregin keys"""

    __tablename__ = "users"
    user_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(200), nullable=False)
    phone_number = Column(String(100), nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    gender = Column(String(100), nullable=False)
    birthdate = Column(DateTime, nullable=False)
    type = Column(String(50))

    __mapper_args__ = {
        'polymorphic_identity': 'user',
        'polymorphic_on': type
    }

    # add cascade
    # default: cascade is false with attributes (save-update, merge)
    patient = relationship('Patient',
                           # primaryjoin="Patient.user_id==User.id",
                           # ADD CASCADE
                           # "all, delete-orphan" to indicate that
                           # related objects should follow along
                           # with the parent object in all cases,
                           # and be deleted when de-associated
                           # add cascade
                           cascade="all, delete, delete-orphan",
                           backref="user",
                           uselist=False)
    doctor = relationship('Doctor',
                          # primaryjoin="Doctor.userd_id==User.id",
                          # add cascade
                          cascade="all, delete, delete-orphan",
                          backref="user",
                          uselist=False)

    def __init__(self, *args, **kwargs):
        """initialization"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """sets password attributes with hash function algorithm SHA-2"""
        if name == "password":
            value = hashlib.sha512(value.encode()).hexdigest()

        super().__setattr__(name, value)

# class UserSchema(SQLAlchemyAutoSchema):
# class UserSchema(SQLAlchemySchema):
#    """marshmallow schema"""
#    class Meta:
#        """class meta"""
#        model = User

#    user_name = auto_field()
#    email = auto_field()
#    password = auto_field()
#    phone_number = auto_field()
#    first_name = auto_field()
#    last_name = auto_field()
#    gender = auto_field()
#    birthdate = auto_field()
#    type = auto_field()

#    __mapper_args__ = auto_field()
#    patient = auto_field()
#    doctor = auto_field()
