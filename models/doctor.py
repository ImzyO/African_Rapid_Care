#!/usr/bin/python3
"""module defines a class Doctor"""


import models
import sqlalchemy
from models.user import User
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy import DateTime
from sqlalchemy.orm import relationship
# import hashlib
# from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


doctor_specialization = Table("doctor_specialization",
                              Base.metadata,
                              Column("doctor_id",
                                     String(60),
                                     ForeignKey('doctors.id'),
                                     primary_key=True,
                                     nullable=False),
                              Column("specialization_id",
                                     String(60),
                                     ForeignKey('specializations.id'),
                                     primary_key=True,
                                     nullable=False))


class Doctor(User):
    """doctor class with attributes of patient"""

    __tablename__ = "doctors"
    id = Column(String(60),
                ForeignKey("users.id"),
                primary_key=True,
                nullable=False)
    # userd_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    doctor_info = Column(String(1024), nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'doctor',
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

    # one to many relationship between doctors and reviews
    reviews = relationship('Review', backref='doctor',
                           # cascade='delete',
                           cascade="all, delete, delete-orphan")

    # many to many between doctors and specializations
    # through doctor_specialization
    specializations = relationship('Specialization',
                                   secondary=doctor_specialization,
                                   viewonly=False,
                                   # backref is pseudo column
                                   # created in Specialization
                                   backref='doctor_specializations')
    # cascade = "all, delete, delete-orphan")
    # one to many relationship between doctors and hospital_affiliation
    hospitals = relationship('HospitalAffiliation',
                             backref="doctor",
                             # cascade='delete',
                             cascade="all, delete, delete-orphan")

    offices = relationship('Office',
                           backref="doctor",
                           cascade="all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        """initialization"""
        super().__init__(*args, **kwargs)

    # def __setattr__(self, name, value):
    #    """sets password attributes with hash function algorithm SHA-2"""
        # if name == "password":
        #    value = hashlib.sha512(value.encode()).hexdigest()
    #    super().__setattr__(name, value)
