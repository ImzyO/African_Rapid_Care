#!/usr/bin/python3
"""
module for testing Specialization class
"""

from datetime import datetime
import inspect
import models
from models.base_model import BaseModel
import pep8
import unittest
from models import specialization
Specialization = specialization.Specialization


class TestSpecializationDocs(unittest.TestCase):
    """Tests to check the documentation and style of Specialization class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.specialization_f = inspect.getmembers(Specialization,
                                                  inspect.isfunction)

    def test_pep8_conformance_specialization(self):
        """Test that models/specialization.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/specialization.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_specialization(self):
        """Test that tests/test_models/test_specialization.py
        conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files([
            'tests/test_models/test_specialization.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_specialization_module_docstring(self):
        """Test for the specialization.py module docstring"""
        self.assertIsNot(specialization.__doc__, None,
                         "specialization.py needs a docstring")
        self.assertTrue(len(specialization.__doc__) >= 1,
                        "specialization.py needs a docstring")

    def test_specialization_class_docstring(self):
        """Test for the Specialization class docstring"""
        self.assertIsNot(Specialization.__doc__, None,
                         "Specialization class needs a docstring")
        self.assertTrue(len(Specialization.__doc__) >= 1,
                        "Specialization class needs a docstring")

    def test_specialization_func_docstrings(self):
        """Test for the presence of docstrings in Specialization methods"""
        for func in self.specialization_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestSpecialization(unittest.TestCase):
    """Test the Specialization class"""
    def test_is_subclass(self):
        """Test that Specialization is a subclass of BaseModel"""
        specialization = Specialization()
        self.assertIsInstance(specialization, BaseModel)
        self.assertTrue(hasattr(specialization, "id"))
        self.assertTrue(hasattr(specialization, "created_at"))
        self.assertTrue(hasattr(specialization, "updated_at"))

    def test_specialization_name_attr(self):
        """Test that Specialization has attr specialization_name,
        and it's an empty string"""
        specialization = Specialization()
        self.assertTrue(hasattr(specialization, "specialization_name"))
        self.assertEqual(specialization.specialization_name, None)

    def test_sp_info_attr(self):
        """Test that Specialization has attr sp_info,
        and it's an empty string"""
        specialization = Specialization()
        self.assertTrue(hasattr(specialization, "sp_info"))
        self.assertEqual(specialization.sp_info, None)

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        s = Specialization()
        new_d = s.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in s.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        s = Specialization()
        new_d = s.to_dict()
        self.assertEqual(new_d["__class__"], "Specialization")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], s.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], s.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        specialization = Specialization()
        string = "[Specialization] ({}) {}".format(specialization.id,
                                                   specialization.__dict__)
        self.assertEqual(string, str(specialization))
