#!/usr/bin/python3
"""module defines a class DoctorSpecialization"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class DoctorSpecialization(Base):
    """patient class with attributes of patient"""

    __tablename = "doctor_specialization"
    doctorspecialization_id = Column(String(60), primary_key=True, nullable=False)
    doctor_id = Column(String(60), ForeignKey('doctors.id'), nullable=False)
    specialization_id = Column(String(60), ForeignKey('specializations.id'), nullable=False)
    ds_info = Column(String(1024), nullable=True)
