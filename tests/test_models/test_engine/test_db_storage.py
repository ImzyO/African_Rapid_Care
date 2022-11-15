#!/usr/bin/python3
"""
module for testing the storage
"""

from datetime import datetime
import inspect
import models
from models.engine import db_storage
from models.base_model import BaseModel, Base
# from models.user import User
from models.patient import Patient
from models.doctor import Doctor
from models.specialization import Specialization
from models.review import Review
from models.hospital_affiliation import HospitalAffiliation
from models.office import Office
from models.office_hours import OfficeHours
from models.appointment import Appointment
from models.appointment_status import AppointmentStatus
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
           "AppointmentStatus": AppointmentStatus}


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
