#!/usr/bin/python3
"""module for database engine"""

import models
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
import os
from models.base_model import BaseModel, Base
from models.user import User
from models.patient import Patient
from models.doctor import Doctor
from models.specialization import Specialization
from models.review import Review
from models.hospital_affiliation import HospitalAffiliation
from models.office import Office
from models.office_hours import OfficeHours
from models.appointment import Appointment
from models.appointment_status import AppointmentStatus
from models.distance import Distance

classes = {"User": User,
           "Patient": Patient, "Doctor": Doctor,
           "Review": Review, "Specialization": Specialization,
           "HospitalAffiliation": HospitalAffiliation,
           "Office": Office, "OfficeHours": OfficeHours,
           "Appointment": Appointment,
           "AppointmentStatus": AppointmentStatus,
           "Distance": Distance}


class DBstorage:
    """database storage"""
    engine = None
    session = None

    def __init__(self):
        """initialization"""
        # {} {} {} {} - name, password, host, database name
        self.engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
            os.environ.get('ARC_MYSQL_USER'),
            os.environ.get('ARC_MYSQL_PASSWORD'),
            os.environ.get('ARC_MYSQL_HOST'),
            os.environ.get('ARC_MYSQL_DB')))

    def all(self, cls=None):
        """query the current database session and return objects
        depending on the class name"""
        dictionary = {}
        for classe in classes:
            if cls is None or cls is classes[classe] or cls is classe:
                objs = self.session.query(classes[classe]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    dictionary[key] = obj
        return dictionary

    def new(self, obj):
        """brand new instancs added"""
        self.session.add(obj)

    def save(self):
        """saves atm transactions"""
        self.session.commit()

    def rollback_session(self):
        """
            rollsback a session in the event of an exception
        """
        self.session.rollback()

    def delete(self, obj=None):
        """method places an instance into the Session’s
        list of objects to be marked as deleted"""
        self.session.delete(obj)
        self.save()

    def reload(self):
        """refreshing objects or when ORM lazy load operations occur"""
        Base.metadata.create_all(self.engine)
        self.session = scoped_session(sessionmaker(
            bind=self.engine, expire_on_commit=False))

    def close(self):
        """ method is more like a “reset” back to the clean state
        and not as much like a “database close” method."""
        self.session.close()

    def get_byID(self, cls, id):
        """returns an object based on class name and ID"""
        if cls not in classes.values():
            return None

        all_cls = models.database_storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value

        return None

    def get_user_byEmail(self, cls, email):
        """returns a User object based on email"""
        if cls is not classes['User']:
            return None

        all_cls = models.database_storage.all(cls)
        for value in all_cls.values():
            if (value.email == email):
                return value

        return None

    def count(self, cls=None):
        """count the number of objects in storage"""
        all_class = classes.values()

        if not cls:
            count = 0
            for clas in all_class:
                count += len(models.database_storage.all(clas).values())
        else:
            count = len(models.database_storage.all(cls).values())

        return count
