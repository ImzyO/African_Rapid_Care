#!/usr/bin/python3
"""module defines the status of an appointment"""
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey
from sqlalchemy.orm import relationship


class AppointmentStatus(BaseModel, Base):
    """class appointment status with attributes"""
    __tablename__ = "appointment_status"

    appointment_status =  Column(String(128), nullable=False)

    appointments = relationship('Appointment', backref='appointmentstatus', cascade='delete')

    def __init__(self, *args, **kwargs):
        """initialization"""
        super().__init__(*args, **kwargs)
