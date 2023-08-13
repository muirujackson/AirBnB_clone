#!/usr/bin/python3
"""Defines unittests for models/base_model.py.

Unittest classes:
    TestBaseModel_instantiation
    TestBaseModel_save
    TestBaseModel_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""

    def test_no_args_instantiates(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_unique_ids(self):
        b_model1 = BaseModel()
        b_model2 = BaseModel()
        self.assertNotEqual(b_model1.id, b_model2.id)

    def test_two_models_different_created_at(self):
        b_model1 = BaseModel()
        sleep(0.05)
        b_model2 = BaseModel()
        self.assertLess(b_model1.created_at, b_model2.created_at)

    def test_two_models_different_updated_at(self):
        b_model1 = BaseModel()
        sleep(0.05)
        b_model2 = BaseModel()
        self.assertLess(b_model1.updated_at, b_model2.updated_at)

    def test_str_representation(self):
        d_time = datetime.today()
        d_time_repr = repr(d_time)
        b_model = BaseModel()
        b_model.id = "123456"
        b_model.created_at = b_model.updated_at = d_time
        b_modelstr = b_model.__str__()
        self.assertIn("[BaseModel] (123456)", b_modelstr)
        self.assertIn("'id': '123456'", b_modelstr)
        self.assertIn("'created_at': " + d_time_repr, b_modelstr)
        self.assertIn("'updated_at': " + d_time_repr, b_modelstr)

    def test_args_unused(self):
        b_model = BaseModel(None)
        self.assertNotIn(None, b_model.__dict__.values())

    def test_instantiation_with_kwargs(self):
        d_time = datetime.today()
        d_time_iso = d_time.isoformat()
        b_model = BaseModel(id="345", created_at=d_time_iso, updated_at=d_time_iso)
        self.assertEqual(b_model.id, "345")
        self.assertEqual(b_model.created_at, d_time)
        self.assertEqual(b_model.updated_at, d_time)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        d_time = datetime.today()
        d_time_iso = d_time.isoformat()
        b_model = BaseModel("12", id="345", created_at=d_time_iso, updated_at=d_time_iso)
        self.assertEqual(b_model.id, "345")
        self.assertEqual(b_model.created_at, d_time)
        self.assertEqual(b_model.updated_at, d_time)


class TestBaseModel_save(unittest.TestCase):
    """Unittests for testing save method of the BaseModel class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        b_model = BaseModel()
        sleep(0.05)
        first_updated_at = b_model.updated_at
        b_model.save()
        self.assertLess(first_updated_at, b_model.updated_at)

    def test_two_saves(self):
        b_model = BaseModel()
        sleep(0.05)
        first_updated_at = b_model.updated_at
        b_model.save()
        second_updated_at = b_model.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        b_model.save()
        self.assertLess(second_updated_at, b_model.updated_at)

    def test_save_with_arg(self):
        b_model = BaseModel()
        with self.assertRaises(TypeError):
            b_model.save(None)

    def test_save_updates_file(self):
        b_model = BaseModel()
        b_model.save()
        b_modelid = "BaseModel." + b_model.id
        with open("file.json", "r") as f:
            self.assertIn(b_modelid, f.read())


class TestBaseModel_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the BaseModel class."""

    def test_to_dict_type(self):
        b_model = BaseModel()
        self.assertTrue(dict, type(b_model.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        b_model = BaseModel()
        self.assertIn("id", b_model.to_dict())
        self.assertIn("created_at", b_model.to_dict())
        self.assertIn("updated_at", b_model.to_dict())
        self.assertIn("__class__", b_model.to_dict())

    def test_to_dict_contains_added_attributes(self):
        b_model = BaseModel()
        b_model.name = "Holberton"
        b_model.my_number = 98
        self.assertIn("name", b_model.to_dict())
        self.assertIn("my_number", b_model.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        b_model = BaseModel()
        b_model_dict = b_model.to_dict()
        self.assertEqual(str, type(b_model_dict["created_at"]))
        self.assertEqual(str, type(b_model_dict["updated_at"]))

    def test_to_dict_output(self):
        d_time = datetime.today()
        b_model = BaseModel()
        b_model.id = "123456"
        b_model.created_at = b_model.updated_at = d_time
        tdict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': d_time.isoformat(),
            'updated_at': d_time.isoformat()
        }
        self.assertDictEqual(b_model.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        b_model = BaseModel()
        self.assertNotEqual(b_model.to_dict(), b_model.__dict__)

    def test_to_dict_with_arg(self):
        b_model = BaseModel()
        with self.assertRaises(TypeError):
            b_model.to_dict(None)


if __name__ == "__main__":
    unittest.main()