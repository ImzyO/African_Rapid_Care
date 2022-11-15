#!/usr/bin/python3
"""
module for testing AppointmentStatus class
"""

from datetime import datetime
import inspect
import models
from models.base_model import BaseModel
import pep8
import unittest
from models import appointment_status
AppointmentStatus = appointment_status.AppointmentStatus


class TestAppointmentStatusDocs(unittest.TestCase):
    """Tests to check the documentation and style of AppointmentStatus class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.appointment_status_f = inspect.getmembers(AppointmentStatus,
                                                      inspect.isfunction)

    def test_pep8_conformance_appointment_status(self):
        """Test that models/appointment_status.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/appointment_status.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_appointment_status(self):
        """Test that tests/test_models/test_appointment_status.py
        conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files([
            'tests/test_models/test_appointment_status.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_appointment_status_module_docstring(self):
        """Test for the appointment_status.py module docstring"""
        self.assertIsNot(appointment_status.__doc__, None,
                         "appointment_status.py needs a docstring")
        self.assertTrue(len(appointment_status.__doc__) >= 1,
                        "appointment_status.py needs a docstring")

    def test_appointment_status_class_docstring(self):
        """Test for the AppointmentStatus class docstring"""
        self.assertIsNot(AppointmentStatus.__doc__, None,
                         "AppointmentStatus class needs a docstring")
        self.assertTrue(len(AppointmentStatus.__doc__) >= 1,
                        "AppointmentStatus class needs a docstring")

    def test_appointment_func_docstrings(self):
        """Test for the presence of docstrings in AppointmentStatus methods"""
        for func in self.appointment_status_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestAppointmentStatus(unittest.TestCase):
    """Test the AppointmentStatus class"""
    def test_is_subclass(self):
        """Test that AppointmentStatus is a subclass of BaseModel"""
        appointment_status = AppointmentStatus()
        self.assertIsInstance(appointment_status, BaseModel)
        self.assertTrue(hasattr(appointment_status, "id"))
        self.assertTrue(hasattr(appointment_status, "created_at"))
        self.assertTrue(hasattr(appointment_status, "updated_at"))

    def test_appointment_status_attr(self):
        """Test that AppointmentStatus has attr
        appointment_status, and it's an empty string"""
        appointment_status = AppointmentStatus()
        self.assertTrue(hasattr(appointment_status, "appointment_status"))
        self.assertEqual(appointment_status.appointment_status, None)

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        r = AppointmentStatus()
        new_d = r.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in r.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        r = AppointmentStatus()
        new_d = r.to_dict()
        self.assertEqual(new_d["__class__"], "AppointmentStatus")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], r.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], r.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        appointment_status = AppointmentStatus()
        string = "[AppointmentStatus] ({}) {}".format(
            appointment_status.id, appointment_status.__dict__)
        self.assertEqual(string, str(appointment_status))
