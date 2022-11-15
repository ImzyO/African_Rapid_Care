#!/usr/bin/python3
"""
module for testing OfficeHours class
"""

from datetime import datetime
import inspect
import models
from models.base_model import BaseModel
import pep8
import unittest
from models import office_hours
OfficeHours = office_hours.OfficeHours


class TestOfficeHoursDocs(unittest.TestCase):
    """Tests to check the documentation and style of OfficeHours class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.office_hours_f = inspect.getmembers(OfficeHours,
                                                inspect.isfunction)

    def test_pep8_conformance_office_hours(self):
        """Test that models/office_hours.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/office_hours.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_office_hours(self):
        """Test that tests/test_models/test_office_hours.py
        conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_office_hours.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_office_hours_module_docstring(self):
        """Test for the office_hours.py module docstring"""
        self.assertIsNot(office_hours.__doc__, None,
                         "office_hours.py needs a docstring")
        self.assertTrue(len(office_hours.__doc__) >= 1,
                        "office_hours.py needs a docstring")

    def test_office_hours_class_docstring(self):
        """Test for the OfficeHours class docstring"""
        self.assertIsNot(OfficeHours.__doc__, None,
                         "OfficeHours class needs a docstring")
        self.assertTrue(len(OfficeHours.__doc__) >= 1,
                        "OfficeHours class needs a docstring")

    def test_office_hours_func_docstrings(self):
        """Test for the presence of docstrings in OfficeHours methods"""
        for func in self.office_hours_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestOfficeHours(unittest.TestCase):
    """Test the OfficeHours class"""
    def test_is_subclass(self):
        """Test that OfficeHours is a subclass of BaseModel"""
        office_hours = OfficeHours()
        self.assertIsInstance(office_hours, BaseModel)
        self.assertTrue(hasattr(office_hours, "id"))
        self.assertTrue(hasattr(office_hours, "created_at"))
        self.assertTrue(hasattr(office_hours, "updated_at"))

    def test_day_of_the_week_attr(self):
        """Test that OfficeHours has attr day_of_the_week,
        and it's an empty string"""
        office_hours = OfficeHours()
        self.assertTrue(hasattr(office_hours, "day_of_the_week"))
        self.assertEqual(office_hours.day_of_the_week, None)

    def test_start_time_attr(self):
        """Test that OfficeHours has attr doctor_id,
        and it's an empty string"""
        office_hours = OfficeHours()
        self.assertTrue(hasattr(office_hours, "start_time"))
        self.assertEqual(office_hours.start_time, None)

    def test_end_time_attr(self):
        """Test that OfficeHours has attr review_info,
        and it's an empty string"""
        office_hours = OfficeHours()
        self.assertTrue(hasattr(office_hours, "end_time"))
        self.assertEqual(office_hours.end_time, None)

    def test_availability_attr(self):
        """Test that OfficeHours has attr review_info,
        and it's an empty string"""
        office_hours = OfficeHours()
        self.assertTrue(hasattr(office_hours, "availability"))
        self.assertEqual(office_hours.availability, None)

    def test_office_id_attr(self):
        """Test that OfficeHours has attr office_id,
        and it's an empty string"""
        office_hours = OfficeHours()
        self.assertTrue(hasattr(office_hours, "office_id"))
        self.assertEqual(office_hours.office_id, None)

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        r = OfficeHours()
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
        r = OfficeHours()
        new_d = r.to_dict()
        self.assertEqual(new_d["__class__"], "OfficeHours")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], r.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], r.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        office_hours = OfficeHours()
        string = "[OfficeHours] ({}) {}".format(
            office_hours.id, office_hours.__dict__)
        self.assertEqual(string, str(office_hours))
