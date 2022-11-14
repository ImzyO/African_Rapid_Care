#!/usr/bin/python3
"""instantiation"""
from models.engine.db_storage import DBstorage 
# from models.base_model import BaseModel, Base
# from models.engine.db_storage import DBstorage
# from models.user import User
# from models.patient import Patient
# from models.doctor import Doctor
# from models.specialization import Specialization
# from models.review import Review
# from models.hospital_affiliation import HospitalAffiliation
# from models.office import Office
# from models.office_hours import OfficeHours
# from models.appointment import Appointment
# from models.appointment_status import AppointmentStatus


database_storage = DBstorage()
database_storage.reload()
