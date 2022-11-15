#!/usr/bin/python3
"""
module for testing Office class
"""

from datetime import datetime
import inspect
import models
from models.base_model import BaseModel
import pep8
import unittest
from models import office
Office = office.Office


class TestOfficeDocs(unittest.TestCase):
    """Tests to check the documentation and style of Office class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.office_f = inspect.getmembers(Office, inspect.isfunction)

    def test_pep8_conformance_office(self):
        """Test that models/office.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/office.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_office(self):
        """Test that tests/test_models/test_office.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_office.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_office_module_docstring(self):
        """Test for the office.py module docstring"""
        self.assertIsNot(office.__doc__, None,
                         "office.py needs a docstring")
        self.assertTrue(len(office.__doc__) >= 1,
                        "office.py needs a docstring")

    def test_office_class_docstring(self):
        """Test for the Office class docstring"""
        self.assertIsNot(Office.__doc__, None,
                         "Office class needs a docstring")
        self.assertTrue(len(Office.__doc__) >= 1,
                        "Office class needs a docstring")

    def test_office_func_docstrings(self):
        """Test for the presence of docstrings in Office methods"""
        for func in self.office_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestOffice(unittest.TestCase):
    """Test the Office class"""
    def test_is_subclass(self):
        """Test that Office is a subclass of BaseModel"""
        office = Office()
        self.assertIsInstance(office, BaseModel)
        self.assertTrue(hasattr(office, "id"))
        self.assertTrue(hasattr(office, "created_at"))
        self.assertTrue(hasattr(office, "updated_at"))

    def test_longitude_attr(self):
        """Test that Office has attr longitude, and it's an empty string"""
        office = Office()
        self.assertTrue(hasattr(office, "longitude"))
        self.assertEqual(office.longitude, None)

    def test_latitude_attr(self):
        """Test that Office has attr latitude, and it's an empty string"""
        office = Office()
        self.assertTrue(hasattr(office, "latitude"))
        self.assertEqual(office.latitude, None)

    def test_country_attr(self):
        """Test that Office has attr country, and it's an empty string"""
        office = Office()
        self.assertTrue(hasattr(office, "country"))
        self.assertEqual(office.country, None)

    def test_city_attr(self):
        """Test that Office has attr city, and it's an empty string"""
        office = Office()
        self.assertTrue(hasattr(office, "city"))
        self.assertEqual(office.city, None)

    def test_office_address_attr(self):
        """Test that Office has attr office_address,
        and it's an empty string"""
        office = Office()
        self.assertTrue(hasattr(office, "office_address"))
        self.assertEqual(office.office_address, None)

    def test_info_attr(self):
        """Test that Office has attr info, and it's an empty string"""
        office = Office()
        self.assertTrue(hasattr(office, "info"))
        self.assertEqual(office.info, None)

    def test_doctor_id_attr(self):
        """Test that Office has attr doctor_id, and it's an empty string"""
        office = Office()
        self.assertTrue(hasattr(office, "doctor_id"))
        self.assertEqual(office.doctor_id, None)

    def test_hospital_id_attr(self):
        """Test that Office has attr hospital_id, and it's an empty string"""
        office = Office()
        self.assertTrue(hasattr(office, "hospital_id"))
        self.assertEqual(office.hospital_id, None)

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        r = Office()
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
        r = Office()
        new_d = r.to_dict()
        self.assertEqual(new_d["__class__"], "Office")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], r.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], r.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        office = Office()
        string = "[Office] ({}) {}".format(office.id, office.__dict__)
        self.assertEqual(string, str(office))
