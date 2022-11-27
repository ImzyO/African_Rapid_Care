#!/usr/bin/python3
"""module defines a class Specialization"""


import models
import sqlalchemy
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
# from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class Specialization(BaseModel, Base):
    """Specialization class"""

    __tablename__ = "specializations"
    specialization_name = Column(String(100), nullable=False)
    sp_info = Column(String(1024), nullable=False)

    # if we created a class DoctorSpecialization,
    # we could add the pseudo column
    # doctor_specializations as follows:
    # doctor_specializations = relationship('DoctorSpecialization',
    #                                       backref='specializations',
    #                                       cascade='delete')

    def __init__(self, *args, **kwargs):
        """initialization"""
        super().__init__(*args, **kwargs)
