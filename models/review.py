#!/usr/bin/python3
"""module defines a class Review"""


import models
import sqlalchemy
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
# from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class Review(BaseModel, Base):
    """Review class"""

    __tablename__ = "reviews"
    patient_id = Column(String(60), ForeignKey('patients.id'), nullable=False)
    doctor_id = Column(String(60), ForeignKey('doctors.id'), nullable=False)
    review_info = Column(String(1024), nullable=False)

    def __init__(self, *args, **kwargs):
        """initialization"""
        super().__init__(*args, **kwargs)
