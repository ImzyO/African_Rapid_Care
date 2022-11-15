#!/usr/bin/python3
"""module defines a class Doctor"""


import models
import sqlalchemy
from models.user import User
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship


doctor_specialization = Table("doctor_specialization", Base.metadata,
                              Column("doctor_id",
                                     String(60),
                                     ForeignKey('doctors.id'),
                                     primary_key=True,
                                     nullable=False),
                              Column("specialization_id",
                                     String(60),
                                     ForeignKey('specializations.id'),
                                     primary_key=True,
                                     nullable=False),
                              Column("ds_info",
                                     String(1024), 
                                     nullable=False)) 

class Doctor(User):
    """doctor class with attributes of patient"""

    __tablename = "doctors"
    userd_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    doctor_info = Column(String(1024), nullable=False)
    
    # one to many relationship between doctors and reviews
    reviews = relationship('Review', backref='doctor', cascade='delete')

    # many to many between doctors and specializations through doctor_specialization
    specializations = relationship('Specialization',
                                   secondary=doctor_specialization,
                                   viewonly=False,
                                   # backref is pseudo column created in Specialization
                                   backref='doctor_specializations')

    # one to many relationship between doctors and hospital_affiliation
    hospitals = relationship('HospitalAffiliation', backref="doctor", cascade='delete')

    def __init__(self, *args, **kwargs):
        """initialization"""
        super().__init__(*args, **kwargs)
