#!/usr/bin/python3
"""module appointments defines time, type and status of appointments"""


import models
import sqlalchemy
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from models.patient import Patient
# from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class Appointment(BaseModel, Base):
    """class defining appointment attributes"""
    __tablename__ = "appointments"

    start_time = Column(DateTime, nullable=False,
                        default=datetime.strptime(str(datetime.utcnow()),
                                                  "%Y-%m-%d %H:%M:%S.%f"))
    end_time = Column(DateTime, nullable=False,
                      default=datetime.strptime(str(datetime.utcnow()),
                                                "%Y-%m-%d %H:%M:%S.%f"))
    symptoms = Column(String(1024), nullable=False)
    appointment_type = Column(String(128), nullable=False)

    office_id = Column(String(60), ForeignKey("offices.id"), nullable=False)
    patient_id = Column(String(60), ForeignKey("patients.id"), nullable=False)
    appointment_status_id = Column(String(60),
                                   ForeignKey("appointment_status.id"),
                                   nullable=False)

    def __init__(self, *args, **kwargs):
        """initialization"""
        super().__init__(*args, **kwargs)
