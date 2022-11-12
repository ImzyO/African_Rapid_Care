#!/usr/bin/python3
"""module defines a class PatientDoctor"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.orm import relationship


class PatientDoctor(Basemodel, Base):
    """patientdoctor class with attributes of patient"""

    __tablename = "patient_doctor"
    patient_id = Column(String(60), ForeignKey('patients.id'), nullable=False)
    doctor_id = Column(String(60), ForeignKey('doctors.id'), nullable=False)
    pd_info = Column(String(1024), nullable=True)

    def __init__(self, *args, **kwargs):
        """initialization"""
        super().__init__(*args, **kwargs)
