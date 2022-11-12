#!/usr/bin/python3
"""module defines a class Doctor"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Doctor(User):
    """doctor class with attributes of patient"""

    __tablename = "doctors"
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    doctor_info = Column(String(1024), nullable=True)
    
    patient_doctor = relationship('PatientDoctor', backref='doctor')

    def __init__(self, *args, **kwargs):
        """initialization"""
        super().__init__(*args, **kwargs)
