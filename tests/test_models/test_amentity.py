#!/usr/bin/python3
"""Defines unittests for models/amenity.py.

Unittest classes:
    TestAmenity_instantiation
    TestAmenity_save
    TestAmenity_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Amenity class."""

    def test_no_args_inst(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instance_in_objects(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_is_str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_datetime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name_is_class_attribute(self):
        amen = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", amen.__dict__)

    def test_two_amenities_unique_ids(self):
        amen1 = Amenity()
        amen2 = Amenity()
        self.assertNotEqual(amen1.id, amen2.id)

    def test_two_amenities_created_at(self):
        amen1 = Amenity()
        sleep(0.05)
        amen2 = Amenity()
        self.assertLess(amen1.created_at, amen2.created_at)

    def test_two_amenities_updated_at(self):
        amen1 = Amenity()
        sleep(0.05)
        amen2 = Amenity()
        self.assertLess(amen1.updated_at, amen2.updated_at)

    def test_str_representation(self):
        dat_time = datetime.today()
        dat_time_repr = repr(dat_time)
        amen = Amenity()
        amen.id = "0123456789"
        amen.created_at = amen.updated_at = dat_time
        amstr = amen.__str__()
        self.assertIn("[Amenity] (0123456789)", amstr)
        self.assertIn("'id': '0123456789'", amstr)
        self.assertIn("'created_at': " + dat_time_repr, amstr)
        self.assertIn("'updated_at': " + dat_time_repr, amstr)

    def test_args_unused(self):
        amen = Amenity(None)
        self.assertNotIn(None, amen.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """instantiation with kwargs test method"""
        dat_time = datetime.today()
        dat_time_iso = dat_time.isoformat()
        amen = Amenity(id="0923", created_at=dat_time_iso, updated_at=dat_time_iso)
        self.assertEqual(amen.id, "0923")
        self.assertEqual(amen.created_at, dat_time)
        self.assertEqual(amen.updated_at, dat_time)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


class TestAmenity_save(unittest.TestCase):
    """Unittests for testing save method of the Amenity class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

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
        amen = Amenity()
        sleep(0.05)
        first_updated_at = amen.updated_at
        amen.save()
        self.assertLess(first_updated_at, amen.updated_at)

    def test_two_saves(self):
        amen = Amenity()
        sleep(0.05)
        first_updated_at = amen.updated_at
        amen.save()
        second_updated_at = amen.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        amen.save()
        self.assertLess(second_updated_at, amen.updated_at)

    def test_save_with_arg(self):
        amen = Amenity()
        with self.assertRaises(TypeError):
            amen.save(None)

    def test_save_updates_file(self):
        amen = Amenity()
        amen.save()
        amenid = "Amenity." + amen.id
        with open("file.json", "r") as f:
            self.assertIn(amenid, f.read())


class TestAmenity_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Amenity class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        amen = Amenity()
        self.assertIn("id", amen.to_dict())
        self.assertIn("created_at", amen.to_dict())
        self.assertIn("updated_at", amen.to_dict())
        self.assertIn("__class__", amen.to_dict())

    def test_to_dict_contains_added_attributes(self):
        amen = Amenity()
        amen.middle_name = "Holberton"
        amen.my_number = 98
        self.assertEqual("Holberton", amen.middle_name)
        self.assertIn("my_number", amen.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        amen = Amenity()
        amen_dict = amen.to_dict()
        self.assertEqual(str, type(amen_dict["id"]))
        self.assertEqual(str, type(amen_dict["created_at"]))
        self.assertEqual(str, type(amen_dict["updated_at"]))

    def test_to_dict_output(self):
        dat_time = datetime.today()
        amen = Amenity()
        amen.id = "123456"
        amen.created_at = amen.updated_at = dat_time
        tdict = {
            'id': '123456',
            '__class__': 'Amenity',
            'created_at': dat_time.isoformat(),
            'updated_at': dat_time.isoformat(),
        }
        self.assertDictEqual(amen.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        amen = Amenity()
        self.assertNotEqual(amen.to_dict(), amen.__dict__)

    def test_to_dict_with_arg(self):
        amen = Amenity()
        with self.assertRaises(TypeError):
            amen.to_dict(None)


if __name__ == "__main__":
    unittest.main()