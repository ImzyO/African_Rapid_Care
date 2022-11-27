#!/usr/bin/python3
"""module defines the status of an appointment"""


import models
import sqlalchemy
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
# from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class AppointmentStatus(BaseModel, Base):
    """class appointment status with attributes"""
    __tablename__ = "appointment_status"

    appointment_status = Column(String(128), nullable=False)

    appointments = relationship('Appointment',
                                backref='appointmentstatus',
                                # cascade='delete',
                                cascade="all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        """initialization"""
        super().__init__(*args, **kwargs)
