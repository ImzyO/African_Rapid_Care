#!/usr/bin/python3
"""module office hours defines hours of operation associated wiith an office"""


import models
import sqlalchemy
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, DateTime
from datetime import datetime
# from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class OfficeHours(BaseModel, Base):
    """class officehours with attributes time, day, availability"""
    __tablename__ = "office_hours"

    day_of_the_week = Column(String(10), nullable=False)
    start_time = Column(DateTime, nullable=False,
                        default=datetime.strptime(str(datetime.utcnow()),
                                                  "%Y-%m-%d %H:%M:%S.%f"))
    end_time = Column(DateTime, nullable=False,
                      default=datetime.strptime(str(datetime.utcnow()),
                                                "%Y-%m-%d %H:%M:%S.%f"))
    availability = Column(String(10), nullable=False)

    office_id = Column(String(60), ForeignKey("offices.id"), nullable=False)

    def __init__(self, *args, **kwargs):
        """initialization"""
        super().__init__(*args, **kwargs)
