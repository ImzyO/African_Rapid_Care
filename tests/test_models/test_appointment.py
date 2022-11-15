#!/usr/bin/python3
"""
module for testing Appointment class
"""

from datetime import datetime
import inspect
import models
from models.base_model import BaseModel
import pep8
import unittest
from models import appointment
Appointment = appointment.Appointment


class TestAppointmentDocs(unittest.TestCase):
    """Tests to check the documentation and style of Appointment class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.appointment_f = inspect.getmembers(Appointment, inspect.isfunction)

    def test_pep8_conformance_appointment(self):
        """Test that models/appointment.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/appointment.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_appointment(self):
        """Test that tests/test_models/test_appointment.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_appointment.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_appointment_module_docstring(self):
        """Test for the appointment.py module docstring"""
        self.assertIsNot(appointment.__doc__, None,
                         "appointment.py needs a docstring")
        self.assertTrue(len(appointment.__doc__) >= 1,
                        "appointment.py needs a docstring")

    def test_appointment_class_docstring(self):
        """Test for the Appointment class docstring"""
        self.assertIsNot(Appointment.__doc__, None,
                         "Appointment class needs a docstring")
        self.assertTrue(len(Appointment.__doc__) >= 1,
                        "Appointment class needs a docstring")

    def test_appointment_func_docstrings(self):
        """Test for the presence of docstrings in Appointment methods"""
        for func in self.appointment_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestAppointment(unittest.TestCase):
    """Test the Appointment class"""
    def test_is_subclass(self):
        """Test that Appointment is a subclass of BaseModel"""
        appointment = Appointment()
        self.assertIsInstance(appointment, BaseModel)
        self.assertTrue(hasattr(appointment, "id"))
        self.assertTrue(hasattr(appointment, "created_at"))
        self.assertTrue(hasattr(appointment, "updated_at"))

    def test_start_time_attr(self):
        """Test that Appointment has attr start_time,
        and it's an empty string"""
        appointment = Appointment()
        self.assertTrue(hasattr(appointment, "start_time"))
        self.assertEqual(appointment.start_time, None)

    def test_end_time_attr(self):
        """Test that Appointment has attr end_time, and it's an empty string"""
        appointment = Appointment()
        self.assertTrue(hasattr(appointment, "end_time"))
        self.assertEqual(appointment.end_time, None)

    def test_symptoms_attr(self):
        """Test that Appointment has attr symptoms, and it's an empty string"""
        appointment = Appointment()
        self.assertTrue(hasattr(appointment, "symptoms"))
        self.assertEqual(appointment.symptoms, None)

    def test_appointment_type_attr(self):
        """Test that Appointment has attr appointment_type,
        and it's an empty string"""
        appointment = Appointment()
        self.assertTrue(hasattr(appointment, "appointment_type"))
        self.assertEqual(appointment.appointment_type, None)

    def test_office_id_attr(self):
        """Test that Appointment has attr office_id,
        and it's an empty string"""
        appointment = Appointment()
        self.assertTrue(hasattr(appointment, "office_id"))
        self.assertEqual(appointment.office_id, None)

    def test_patient_id_attr(self):
        """Test that Appointment has attr patient_id,
        and it's an empty string"""
        appointment = Appointment()
        self.assertTrue(hasattr(appointment, "patient_id"))
        self.assertEqual(appointment.patient_id, None)

    def test_appointment_status_id_attr(self):
        """Test that Appointment has attr appointment_status_id,
        and it's an empty string"""
        appointment = Appointment()
        self.assertTrue(hasattr(appointment, "patient_id"))
        self.assertEqual(appointment.appointment_status_id, None)

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        a = Appointment()
        new_d = a.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in a.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        a = Appointment()
        new_d = a.to_dict()
        self.assertEqual(new_d["__class__"], "Appointment")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], a.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], a.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        appointment = Appointment()
        string = "[Appointment] ({}) {}".format(
            appointment.id, appointment.__dict__)
        self.assertEqual(string, str(appointment))
