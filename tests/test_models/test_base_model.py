#!/usr/bin/python3
"""module for testing base_model.py """


from datetime import datetime
import inspect
import models
import pep8 as pycodestyle
import time
import unittest
from unittest import mock
BaseModel = models.base_model.BaseModel
module_doc = models.base_model.__doc__


class TestBaseModelDocs(unittest.TestCase):
    """Tests to check the documentation and style of BaseModel class"""

    @classmethod
    def setUpClass(self):
        """Set up for docstring tests"""
        self.base_funcs = inspect.getmembers(BaseModel, inspect.isfunction)

    def test_pep8_conformance(self):
        """Test that models/base_model.py conforms to PEP8."""
        for path in ['models/base_model.py',
                     'tests/test_models/test_base_model.py']:
            with self.subTest(path=path):
                errors = pycodestyle.Checker(path).check_all()
                self.assertEqual(errors, 0)

    def test_module_docstring(self):
        """Test for the existence of module docstring"""
        self.assertIsNot(module_doc, None,
                         "base_model.py needs a docstring")
        self.assertTrue(len(module_doc) > 1,
                        "base_model.py needs a docstring")

    def test_class_docstring(self):
        """Test for the BaseModel class docstring"""
        self.assertIsNot(BaseModel.__doc__, None,
                         "BaseModel class needs a docstring")
        self.assertTrue(len(BaseModel.__doc__) >= 1,
                        "BaseModel class needs a docstring")

    def test_func_docstrings(self):
        """Test for the presence of docstrings in BaseModel methods"""
        for func in self.base_funcs:
            with self.subTest(function=func):
                self.assertIsNot(
                    func[1].__doc__,
                    None,
                    "{:s} method needs a docstring".format(func[0])
                )
                self.assertTrue(
                    len(func[1].__doc__) > 1,
                    "{:s} method needs a docstring".format(func[0])
                )


class TestBaseModel(unittest.TestCase):
    """class tests base model class"""
    def test_instantiation(self):
        """tests objects are created"""
        obj1 = BaseModel()
        self.assertIs(type(obj1), BaseModel)

        obj1.name = "Nabil"
        obj1.country = "Togo"

        attributes = {
                "id": str,
                "created_at": datetime,
                "updated_at": datetime,
                "name": str,
                "country": str
                }

        for key, value in attributes.items():
            with self.subTest(key=key, value=value):
                self.assertIn(key, obj1.__dict__, "object not created")
                self.assertIs(type(obj1.__dict__[key]), value,
                              "object attribute not of correct type")

        self.assertEqual(obj1.name, "Nabil")
        self.assertEqual(obj1.country, "Togo")

    def test_date_time_attributes(self):
        """tests two different instances and compares their values"""
        tic = datetime.now()
        inst1 = BaseModel()
        toc = datetime.now()
        self.assertTrue(tic <= inst1.created_at <= toc)
        time.sleep(1e-4)
        tic = datetime.now()
        inst2 = BaseModel()
        toc = datetime.now()
        self.assertTrue(tic <= inst2.created_at <= toc)
        self.assertEqual(inst1.created_at, inst1.updated_at)
        self.assertEqual(inst2.created_at, inst2.updated_at)
        self.assertNotEqual(inst1.created_at, inst2.created_at)
        self.assertNotEqual(inst1.updated_at, inst2.updated_at)

    def test_uuid(self):
        """Test that id is a valid uuid: note: assertRegex
        checks the uuid format (8-4-4-12)digits"""
        inst1 = BaseModel()
        inst2 = BaseModel()
        for inst in [inst1, inst2]:
            uuid = inst.id
            with self.subTest(uuid=uuid):
                self.assertIs(type(uuid), str)
                self.assertRegex(uuid,
                                 '^[0-9a-f]{8}-[0-9a-f]{4}'
                                 '-[0-9a-f]{4}-[0-9a-f]{4}'
                                 '-[0-9a-f]{12}$')
        self.assertNotEqual(inst1.id, inst2.id)

    def test_str(self):
        """test that the str magic method has the correct output"""
        inst = BaseModel()
        string = "[BaseModel] ({}) {}".format(inst.id, inst.__dict__)
        self.assertEqual(string, str(inst))

    def test_to_dict(self):
        """tests objects within dictionary(types, values)"""
        my_model = BaseModel()
        my_model.name = "Imani"
        my_model.my_number = 22
        d = my_model.to_dict()
        expected_attrs = ["id",
                          "created_at",
                          "updated_at",
                          "name",
                          "my_number",
                          "__class__"]
        self.assertCountEqual(d.keys(), expected_attrs)
        self.assertEqual(d['__class__'], 'BaseModel')
        self.assertEqual(d['name'], "Imani")
        self.assertEqual(d['my_number'], 22)

        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.assertEqual(d["__class__"], "BaseModel")
        self.assertEqual(type(d["created_at"]), str)
        self.assertEqual(type(d["updated_at"]), str)
        self.assertEqual(d["created_at"],
                         my_model.created_at.strftime(t_format))
        self.assertEqual(d["updated_at"],
                         my_model.updated_at.strftime(t_format))

    @mock.patch('models.database_storage')
    def test_save(self, mock_storage):
        """Test that save method updates `updated_at` and calls
        `storage.save`"""
        inst = BaseModel()
        old_created_at = inst.created_at
        old_updated_at = inst.updated_at
        inst.save()
        new_created_at = inst.created_at
        new_updated_at = inst.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertEqual(old_created_at, new_created_at)
        self.assertTrue(mock_storage.new.called)
        self.assertTrue(mock_storage.save.called)

    # @mock.patch('models.database_storage')
    # def test_delete(self, mock_storage):
    #    """tests that objects are deleted"""
    #    inst = BaseModel()
    #    inst.delete()
    #    self.assertEqual(inst.created_at, None)
    #    self.assertEqual(inst.created_at, None)
    #    self.assertEqual(inst.id, None)
    #    self.assertTrue(mock_storage.delete.called)
