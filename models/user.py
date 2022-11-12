#!/usr/bin/python3
"""
module defines a class user: who could be a patient/doctor:
attributes apply to both as they are both users
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import hashlib


class User(BaseModel, Base):
    """user class with attributes of user"""
    """user relates to doctor and patient modules via Foregin keys"""

    __tablename__ = "users"
    user_name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(200), nullable=False)
    phone_number = Column(String(100), nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    gender = Column(String(100), nullable=False)
    birthday = Column(String(100), nullable=False)

    patient = relationship('Patient', backref='user')
    doctor = relationship('Doctor', backref='user')

    def __init__(self, *args, **kwargs):
        """initialization"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """sets password attributes with hash function algorithm SHA-2"""
        if name == "password":
            value = hashlib.sha512(value.encode()).hexdigest()

        super().__setattr__(name, value)
