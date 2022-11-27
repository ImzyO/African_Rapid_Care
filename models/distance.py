#!/usr/bin/python3
"""
module defines a class Distance
"""

import requests
import models
import sqlalchemy
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Float, ForeignKey
# from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class Distance(BaseModel, Base):
    """Distance class: represents the distance between
    a user in common metrics"""

    __tablename__ = "distances"
    patient_id = Column(String(60), ForeignKey('patients.id'), nullable=False)
    office_id = Column(String(60), ForeignKey('offices.id'), nullable=False)
    distance_text = Column(String(60), nullable=False)
    distance = Column(Float, nullable=False)

    def __init__(self, *args, **kwargs):
        """initialization"""
        super().__init__(*args, **kwargs)

    """
    def __setattr__(self, name, value):
        # return distance
        origin =  latitude, longitude
        destination = latitude, longitude
        url = "https://maps.googleapis.com/maps/api/distancematrix/json?"
        API_key = "AIzaSyBIMGTpeGByzmmMcBnLCj-6SLCulwVHkao"
    """
