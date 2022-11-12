#!/usr/bin/python3
"""module appointments defines time, type and status of appointments"""
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey, DateTime
from datetime import datetime

class Appointments(BaseModel, Base):
    """class defining appointment attributes"""
    __tablename__ = "appointments"

    start_time = Column(DateTime(128), nullable=False, default=datetime.utcnow()))
    end_time = Column(DateTime(128), nullable=False, default=datetime.utcnow()))
    symptoms = Column(String(128), nullable=False)
    appointment_type = Column(String(128), nullable=False)
    
    office_id = Column(String(60), ForeignKey("offices.id"), nullable=False)
    patient_id = Column(String(60), ForeignKey("patients.id"), nullable=False) #refer with Nabil
    appointment_status_id = Column(String(60), ForeignKey("appointment_status.id"), nullable=False)
