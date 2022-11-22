#!/usr/bin/python3
"""
module defines a class Distance
"""


import models
import sqlalchemy
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Float, ForeignKey


class Distance(BaseModel, Base):
    """Distance class: represents the distance between
    a user in common metrics"""

    __tablename__ = "distances"
    patient_id = Column(String(60), ForeignKey('patients.id'), nullable=False)
    office_id = Column(String(60), ForeignKey('offices.id'), nullable=False)
    distance = Column(Float, nullable=False)

    def __init__(self, *args, **kwargs):
        """initialization"""
        super().__init__(*args, **kwargs)
