#!/usr/bin/python3
"""module serving associated hospital"""

import models
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
# from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class HospitalAffiliation(BaseModel, Base):
    """class associating with hospital"""
    __tablename__ = "hospital_affiliation"

    hospital_name = Column(String(100), nullable=False)
    hospital_phone_number = Column(String(100), nullable=False)
    hospital_country = Column(String(100), nullable=False)
    hospital_city = Column(String(100), nullable=False)
    hospital_address = Column(String(100), nullable=False)
    hospital_type = Column(String(100), nullable=False)

    doctor_id = Column(String(60), ForeignKey('doctors.id'), nullable=False)

    offices = relationship('Office',
                           backref='hospitalaffiliation',
                           # cascade='delete'
                           cascade="all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        """initialization"""
        super().__init__(*args, **kwargs)
