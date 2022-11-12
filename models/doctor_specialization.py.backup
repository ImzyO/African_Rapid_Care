#!/usr/bin/python3
"""module defines a class DoctorSpecialization"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, MetaData
from sqlalchemy.orm import relationship


class DoctorSpecialization(Base):
    """DoctorSpecialization class"""

    __tablename = "doctor_specialization"
    metadata = Base.metadata
    doctor_id = Column(String(60), ForeignKey('doctors.id'), primary_key=True, nullable=False)
    specialization_id = Column(String(60), ForeignKey('specializations.id'), primary_key=True, nullable=False)
    ds_info = Column(String(1024), nullable=True)
