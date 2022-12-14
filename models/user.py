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


class User(BaseModel, Base, UserMixin):
    """user class with attributes of user
    user relates to doctor and patient modules via Foregin keys"""

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

    patient = relationship('Patient',
                           cascade="all, delete, delete-orphan",
                           backref="user",
                           uselist=False)
    doctor = relationship('Doctor',
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
