#!/usr/bin/python3
"""module defines the status of an appointment"""
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey



class AppointmentStatus(BaseModel, Base):
    """class appointment status with attributes"""
    __tablename__ = "appointment_status"

    appointment_status =  Column(String(128), nullable=False)
