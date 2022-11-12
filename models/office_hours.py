#!/usr/bin/python3
"""module office hours defines hours of operation associated wiith an office"""
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey, DateTime
from datetime import datetime


class OfficeHours(BaseModel, Base):
    """class officehours with attributes time, day, availability"""
    __tablename__ = "office_hours"

    day_of_the_week = Column(DateTime(128), nullable=False, default=datetime.now().weekday())
    start_time = Column(DateTime(128), nullable=False, default=datetime.utcnow()))
    end_time = Column(DateTime(128), nullable=False, default=datetime.utcnow()))
    availability = Column(DateTime(128), nullable=False) #time or a string(not in office, available)

    office_id = Column(String(60), ForeignKey("offices.id"), nullable=False)
