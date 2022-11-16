#!/usr/bin/python3
"""
module for testing User class
"""

from datetime import datetime
import inspect
import models
from models.base_model import BaseModel
import pep8
import unittest
from models import patient
from models import user
Patient = patient.Patient
User = user.User


class TestPatientDocs(unittest.TestCase):
    """Tests to check the documentation and style of Patient class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.patient_f = inspect.getmembers(Patient, inspect.isfunction)

    def test_pep8_conformance_patient(self):
        """Test that models/patient.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/patient.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_patient(self):
        """Test that tests/test_models/test_patient.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_patient.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_patient_module_docstring(self):
        """Test for the patient.py module docstring"""
        self.assertIsNot(patient.__doc__, None,
                         "patient.py needs a docstring")
        self.assertTrue(len(patient.__doc__) >= 1,
                        "patient.py needs a docstring")

    def test_patient_class_docstring(self):
        """Test for the Patient class docstring"""
        self.assertIsNot(Patient.__doc__, None,
                         "Patient class needs a docstring")
        self.assertTrue(len(Patient.__doc__) >= 1,
                        "Patient class needs a docstring")

    def test_patient_func_docstrings(self):
        """Test for the presence of docstrings in Patient methods"""
        for func in self.patient_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestPatient(unittest.TestCase):
    """Test the Patient class"""
    def test_is_subclass(self):
        """Test that Patient is a subclass of User"""
        patient = Patient()
        self.assertIsInstance(patient, User)
        self.assertTrue(hasattr(patient, "id"))
        self.assertTrue(hasattr(patient, "created_at"))
        self.assertTrue(hasattr(patient, "updated_at"))

    def test_user_name_attr(self):
        """Test that Patient has attr user_name, and it's an empty string"""
        patient = Patient()
        self.assertTrue(hasattr(patient, "user_name"))
        self.assertEqual(patient.user_name, None)

    def test_email_attr(self):
        """Test that Patient has attr email, and it's an empty string"""
        patient = Patient()
        self.assertTrue(hasattr(patient, "email"))
        self.assertEqual(patient.email, None)

    def test_password_attr(self):
        """Test that Patient has attr password, and it's an empty string"""
        patient = Patient()
        self.assertTrue(hasattr(patient, "password"))
        self.assertEqual(patient.password, None)

    def test_phone_number_attr(self):
        """Test that Patient has attr phone_number, and it's an empty string"""
        patient = Patient()
        self.assertTrue(hasattr(patient, "phone_number"))
        self.assertEqual(patient.phone_number, None)

    def test_first_name_attr(self):
        """Test that Patient has attr first_name, and it's an empty string"""
        patient = Patient()
        self.assertTrue(hasattr(patient, "first_name"))
        self.assertEqual(patient.first_name, None)

    def test_last_name_attr(self):
        """Test that Patient has attr last_name, and it's an empty string"""
        patient = Patient()
        self.assertTrue(hasattr(patient, "last_name"))
        self.assertEqual(patient.last_name, None)

    def test_gender_attr(self):
        """Test that Patient has attr gender, and it's an empty string"""
        patient = Patient()
        self.assertTrue(hasattr(patient, "gender"))
        self.assertEqual(patient.gender, None)

    # def test_user_id_attr(self):
    #    """Test that Patient has attr user_id, and it's an empty string"""
    #    patient = Patient()
    #    self.assertTrue(hasattr(patient, "user_id"))
    #    self.assertEqual(patient.user_id, None)

    def test_latitude_attr(self):
        """Test that Patient has attr latitude, and it's an empty string"""
        patient = Patient()
        self.assertTrue(hasattr(patient, "latitude"))
        self.assertEqual(patient.latitude, None)

    def test_longitude_attr(self):
        """Test that Patient has attr longitude, and it's an empty string"""
        patient = Patient()
        self.assertTrue(hasattr(patient, "longitude"))
        self.assertEqual(patient.longitude, None)

    def test_country_attr(self):
        """Test that Patient has attr country, and it's an empty string"""
        patient = Patient()
        self.assertTrue(hasattr(patient, "country"))
        self.assertEqual(patient.country, None)

    def test_city_attr(self):
        """Test that Patient has attr city, and it's an empty string"""
        patient = Patient()
        self.assertTrue(hasattr(patient, "city"))
        self.assertEqual(patient.city, None)

    def test_address_attr(self):
        """Test that Patient has attr address, and it's an empty string"""
        patient = Patient()
        self.assertTrue(hasattr(patient, "address"))
        self.assertEqual(patient.address, None)

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        p = Patient()
        new_d = p.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in p.__dict__:
            # if attr is not "_sa_instance_state":
            if attr != "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        p = Patient()
        new_d = p.to_dict()
        self.assertEqual(new_d["__class__"], "Patient")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], p.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], p.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        patient = Patient()
        string = "[Patient] ({}) {}".format(patient.id, patient.__dict__)
        self.assertEqual(string, str(patient))
