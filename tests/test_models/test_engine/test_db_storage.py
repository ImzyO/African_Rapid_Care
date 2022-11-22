#!/usr/bin/python3
"""
module for testing the storage
"""

from datetime import datetime
import inspect
import models
from models.engine import db_storage
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
import os
import pep8
import unittest
from models import database_storage
DBstorage = db_storage.DBstorage

classes = {"Patient": Patient, "Doctor": Doctor,
           "Review": Review, "Specialization": Specialization,
           "HospitalAffiliation": HospitalAffiliation,
           "Office": Office, "OfficeHours": OfficeHours,
           "Appointment": Appointment,
           "AppointmentStatus": AppointmentStatus,
           "Distance": Distance}


class TestDBstorageDocs(unittest.TestCase):
    """check the documentation and style of DBstorage class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.dbs_f = inspect.getmembers(DBstorage, inspect.isfunction)

    def test_pep8_conformance_db_storage(self):
        """Test that models/engine/db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_db_storage(self):
        """Test tests/test_models/test_db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_engine/\
test_db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_db_storage_module_docstring(self):
        """Test for the db_storage.py module docstring"""
        self.assertIsNot(db_storage.__doc__, None,
                         "db_storage.py needs a docstring")
        self.assertTrue(len(db_storage.__doc__) >= 1,
                        "db_storage.py needs a docstring")

    def test_db_storage_class_docstring(self):
        """Test for the DBstorage class docstring"""
        self.assertIsNot(DBstorage.__doc__, None,
                         "DBstorage class needs a docstring")
        self.assertTrue(len(DBstorage.__doc__) >= 1,
                        "DBstorage class needs a docstring")

    def test_dbs_func_docstrings(self):
        """Test for the presence of docstrings in DBStorage methods"""
        for func in self.dbs_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestDBstorage(unittest.TestCase):
    """Test DBstorage"""
    def test_get_byID(self):
        """Test if get returns an object or not"""
        new_user = User()
        new_user.user_name = "user_name"
        new_user.email = "email@gmail.com"
        new_user.password = "password"
        new_user.first_name = "first_name"
        new_user.last_name = "last_name"
        new_user.birthdate = datetime.now()
        new_user.gender = "gender"
        new_user.phone_number = "phone_number"
        new_user.country = "country"
        new_user.city = "city"
        new_user.address = "user address"
        new_user.save()
        print(new_user.id)
        self.assertIs(new_user,
                      models.database_storage.get_byID(User, new_user.id))
        self.assertIs(None,
                      models.database_storage.get_byID(User, "fake id"))
        self.assertIs(None,
                      models.database_storage.get_byID("fake_class",
                                                       "fake id"))

    def test_get_user_byEmail(self):
        """Test if get returns a User object by email or not"""
        new_user = User()
        new_user.user_name = "user_name"
        new_user.email = "email@gmail.com"
        new_user.password = "password"
        new_user.first_name = "first_name"
        new_user.last_name = "last_name"
        new_user.birthdate = datetime.now()
        new_user.gender = "gender"
        new_user.phone_number = "phone_number"
        new_user.country = "country"
        new_user.city = "city"
        new_user.address = "user address"
        new_user.save()
        print(new_user.email)
        self.assertIs(new_user,
                      models.database_storage.get_user_byEmail(
                          User, new_user.email))
        self.assertIs(None, models.database_storage.get_user_byEmail(
            User, "fake_email@gmail.com"))
        self.assertIs(None,
                      models.database_storage.get_user_byEmail(
                          "fake_class",
                          "fake_email@gmail.com"))

    def test_count(self):
        """Test if count returns the number of objects"""
        first = models.database_storage.count()
        self.assertEqual(models.database_storage.count("shdgkshj"), 0)
        new_user = User()
        new_user.user_name = "user_name"
        new_user.email = "email@gmail.com"
        new_user.password = "password"
        new_user.first_name = "first_name"
        new_user.last_name = "last_name"
        new_user.birthdate = datetime.now()
        new_user.gender = "gender"
        new_user.phone_number = "phone_number"
        new_user.country = "country"
        new_user.city = "city"
        new_user.address = "user address"
        new_user.save()

        new_user2 = User()
        new_user2.user_name = "user_name2"
        new_user2.email = "email2@gmail.com"
        new_user2.password = "password2"
        new_user2.first_name = "first_name2"
        new_user2.last_name = "last_name2"
        new_user2.birthdate = datetime.now()
        new_user2.gender = "gender2"
        new_user2.phone_number = "phone_number2"
        new_user2.country = "country2"
        new_user2.city = "city2"
        new_user2.address = "user address2"
        new_user2.save()

        new_user3 = User()
        new_user3.user_name = "user_name3"
        new_user3.email = "email3@gmail.com"
        new_user3.password = "password3"
        new_user3.first_name = "first_name3"
        new_user3.last_name = "last_name3"
        new_user3.birthdate = datetime.now()
        new_user3.gender = "gender3"
        new_user3.phone_number = "phone_number3"
        new_user3.country = "country3"
        new_user3.city = "city3"
        new_user3.address = "user address3"
        new_user3.save()

        expected = first + 3
        expected_users = first + 3
        self.assertEqual(models.database_storage.count("User"),
                         expected_users)
        self.assertEqual(models.database_storage.count(), expected)
