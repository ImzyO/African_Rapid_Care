#!/usr/bin/python3
"""
module for testing HospitalAffiliation class
"""

from datetime import datetime
import inspect
import models
from models.base_model import BaseModel
import pep8
import unittest
from models import hospital_affiliation
HospitalAffiliation = hospital_affiliation.HospitalAffiliation


class TestHospitalAffiliationDocs(unittest.TestCase):
    """Tests to check the documentation and style of
    HospitalAffiliation class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.hospital_affiliation_f = inspect.getmembers(HospitalAffiliation,
                                                        inspect.isfunction)

    def test_pep8_conformance_hospital_affiliation(self):
        """Test that models/hospital_affiliation.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/hospital_affiliation.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_hospital_affiliation(self):
        """Test that tests/test_models/test_hospital_affiliation.py
        conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files([
            'tests/test_models/test_hospital_affiliation.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_hospital_affiliation_module_docstring(self):
        """Test for the hospital_affiliation.py module docstring"""
        self.assertIsNot(hospital_affiliation.__doc__, None,
                         "hospital_affiliation.py needs a docstring")
        self.assertTrue(len(hospital_affiliation.__doc__) >= 1,
                        "hospital_affiliation.py needs a docstring")

    def test_hospital_affiliation_class_docstring(self):
        """Test for the HospitalAffiliation class docstring"""
        self.assertIsNot(HospitalAffiliation.__doc__, None,
                         "HospitalAffiliation class needs a docstring")
        self.assertTrue(len(HospitalAffiliation.__doc__) >= 1,
                        "HospitalAffiliation class needs a docstring")

    def test_hospital_affiliation_func_docstrings(self):
        """Test for the presence of docstrings in
        HospitalAffiliation methods"""
        for func in self.hospital_affiliation_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestHospitalAffiliation(unittest.TestCase):
    """Test the HospitalAffiliation class"""
    def test_is_subclass(self):
        """Test that HospitalAffiliation is a subclass of BaseModel"""
        hospital_affiliation = HospitalAffiliation()
        self.assertIsInstance(hospital_affiliation, BaseModel)
        self.assertTrue(hasattr(hospital_affiliation, "id"))
        self.assertTrue(hasattr(hospital_affiliation, "created_at"))
        self.assertTrue(hasattr(hospital_affiliation, "updated_at"))

    def test_hospital_name_attr(self):
        """Test that HospitalAffiliation has attr
        hospital_name, and it's an empty string"""
        hospital_affiliation = HospitalAffiliation()
        self.assertTrue(hasattr(hospital_affiliation, "hospital_name"))
        self.assertEqual(hospital_affiliation.hospital_name, None)

    def test_hospital_phone_number_attr(self):
        """Test that HospitalAffiliation has attr
        hospital_phone_number, and it's an empty string"""
        hospital_affiliation = HospitalAffiliation()
        self.assertTrue(hasattr(hospital_affiliation, "hospital_phone_number"))
        self.assertEqual(hospital_affiliation.hospital_phone_number, None)

    def test_hospital_country_attr(self):
        """Test that HospitalAffiliation has attr
        hospital_country, and it's an empty string"""
        hospital_affiliation = HospitalAffiliation()
        self.assertTrue(hasattr(hospital_affiliation, "hospital_country"))
        self.assertEqual(hospital_affiliation.hospital_country, None)

    def test_hospital_city_number_attr(self):
        """Test that HospitalAffiliation has attr
        hospital_city, and it's an empty string"""
        hospital_affiliation = HospitalAffiliation()
        self.assertTrue(hasattr(hospital_affiliation, "hospital_city"))
        self.assertEqual(hospital_affiliation.hospital_city, None)

    def test_hospital_address_attr(self):
        """Test that HospitalAffiliation has attr
        hospital_address, and it's an empty string"""
        hospital_affiliation = HospitalAffiliation()
        self.assertTrue(hasattr(hospital_affiliation, "hospital_address"))
        self.assertEqual(hospital_affiliation.hospital_address, None)

    def test_hospital_type_attr(self):
        """Test that HospitalAffiliation has attr
        hospital_type, and it's an empty string"""
        hospital_affiliation = HospitalAffiliation()
        self.assertTrue(hasattr(hospital_affiliation, "hospital_type"))
        self.assertEqual(hospital_affiliation.hospital_type, None)

    def test_doctor_id_attr(self):
        """Test that HospitalAffiliation has attr
        hospital_doctor_id, and it's an empty string"""
        hospital_affiliation = HospitalAffiliation()
        self.assertTrue(hasattr(hospital_affiliation, "doctor_id"))
        self.assertEqual(hospital_affiliation.doctor_id, None)

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        r = HospitalAffiliation()
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
        r = HospitalAffiliation()
        new_d = r.to_dict()
        self.assertEqual(new_d["__class__"], "HospitalAffiliation")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], r.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], r.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        hospital_affiliation = HospitalAffiliation()
        string = "[HospitalAffiliation] ({}) {}".format(
            hospital_affiliation.id, hospital_affiliation.__dict__)
        self.assertEqual(string, str(hospital_affiliation))
