#!/usr/bin/python3
"""module defines a class Doctor"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship


doctor_specialization = Table("doctor_specialization", Base.metadata,
                              Column("doctor_id",
                                     String(60),
                                     ForeignKey('doctors.id'),
                                     primary_key=True,
                                     nullable=False),
                              Column("specialization_id",
                                     String(60),
                                     ForeignKey('specializations.id'),
                                     primary_key=True,
                                     nullable=False),
                              Column("ds_info",
                                     String(1024), 
                                     nullable=False)) 

class Doctor(User):
    """doctor class with attributes of patient"""

    __tablename = "doctors"
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    doctor_info = Column(String(1024), nullable=False)
    
    # one to many relationship between doctors and reviews
    reviews = relationship('Review', backref='doctor', cascade='delete')

    # many to many between Doctor and Specialization through doctor_specialization
    specializations = relationship('Specialization',
                                   secondary=doctor_specialization,
                                   viewonly=False,
                                   # backref is pseudo column created in Specialization
                                   backref='doctor_specializations')
    
    
    def __init__(self, *args, **kwargs):
        """initialization"""
        super().__init__(*args, **kwargs)
