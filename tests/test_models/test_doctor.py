#!/usr/bin/python3
"""
module for testing Doctor class
"""

from datetime import datetime
import inspect
import models
from models.base_model import BaseModel
import pep8
import unittest
from models import doctor
from models import user
Doctor = doctor.Doctor
User = user.User


class TestDoctorDocs(unittest.TestCase):
    """Tests to check the documentation and style of Doctor class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.doctor_f = inspect.getmembers(Doctor, inspect.isfunction)

    def test_pep8_conformance_doctor(self):
        """Test that models/doctor.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/doctor.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_doctor(self):
        """Test that tests/test_models/test_doctor.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_doctor.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_doctor_module_docstring(self):
        """Test for the doctor.py module docstring"""
        self.assertIsNot(doctor.__doc__, None,
                         "doctor.py needs a docstring")
        self.assertTrue(len(doctor.__doc__) >= 1,
                        "doctor.py needs a docstring")

    def test_doctor_class_docstring(self):
        """Test for the Doctor class docstring"""
        self.assertIsNot(Doctor.__doc__, None,
                         "Doctor class needs a docstring")
        self.assertTrue(len(Doctor.__doc__) >= 1,
                        "Doctor class needs a docstring")

    def test_doctor_func_docstrings(self):
        """Test for the presence of docstrings in Doctor methods"""
        for func in self.doctor_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestDoctor(unittest.TestCase):
    """Test the Doctor class"""
    def test_is_subclass(self):
        """Test that Doctor is a subclass of User"""
        doctor = Doctor()
        self.assertIsInstance(doctor, User)
        self.assertTrue(hasattr(doctor, "id"))
        self.assertTrue(hasattr(doctor, "created_at"))
        self.assertTrue(hasattr(doctor, "updated_at"))

    def test_user_name_attr(self):
        """Test that Doctor has attr user_name, and it's an empty string"""
        doctor = Doctor()
        self.assertTrue(hasattr(doctor, "user_name"))
        self.assertEqual(doctor.user_name, None)

    def test_email_attr(self):
        """Test that Doctor has attr email, and it's an empty string"""
        doctor = Doctor()
        self.assertTrue(hasattr(doctor, "email"))
        self.assertEqual(doctor.email, None)

    def test_password_attr(self):
        """Test that Doctor has attr password, and it's an empty string"""
        doctor = Doctor()
        self.assertTrue(hasattr(doctor, "password"))
        self.assertEqual(doctor.password, None)

    def test_phone_number_attr(self):
        """Test that Doctor has attr phone_number, and it's an empty string"""
        doctor = Doctor()
        self.assertTrue(hasattr(doctor, "phone_number"))
        self.assertEqual(doctor.phone_number, None)

    def test_first_name_attr(self):
        """Test that Doctor has attr first_name, and it's an empty string"""
        doctor = Doctor()
        self.assertTrue(hasattr(doctor, "first_name"))
        self.assertEqual(doctor.first_name, None)

    def test_last_name_attr(self):
        """Test that Doctor has attr last_name, and it's an empty string"""
        doctor = Doctor()
        self.assertTrue(hasattr(doctor, "last_name"))
        self.assertEqual(doctor.last_name, None)

    def test_gender_attr(self):
        """Test that Doctor has attr gender, and it's an empty string"""
        doctor = Doctor()
        self.assertTrue(hasattr(doctor, "gender"))
        self.assertEqual(doctor.gender, None)

    def test_birthdate_attr(self):
        """Test that Doctor has attr birthdate, and it's an empty string"""
        doctor = Doctor()
        self.assertTrue(hasattr(doctor, "birthdate"))
        self.assertEqual(doctor.birthdate, None)

    def test_doctor_info_attr(self):
        """Test that Doctor has attr doctor_info, and it's an empty string"""
        doctor = Doctor()
        self.assertTrue(hasattr(doctor, "doctor_info"))
        self.assertEqual(doctor.doctor_info, None)

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        d = Doctor()
        new_d = d.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in d.__dict__:
            # if attr is not "_sa_instance_state":
            if attr != "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        d = Doctor()
        new_d = d.to_dict()
        self.assertEqual(new_d["__class__"], "Doctor")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], d.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], d.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        doctor = Doctor()
        string = "[Doctor] ({}) {}".format(doctor.id, doctor.__dict__)
        self.assertEqual(string, str(doctor))
