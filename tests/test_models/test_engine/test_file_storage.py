#!/usr/bin/python3
"""Test module"""
import json
import os
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """Unittests for testing FileStorage class"""

    def test_no_args(self):
        self.assertEqual(FileStorage, type(FileStorage()))

    def test_file_path(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_object(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage(self):
        self.assertEqual(type(models.storage), FileStorage)

class TestFileStorage_methods(unittest.TestCase):
    """Unit testing methods of FileStorage"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "file_tmp")
        except IOError:
            pass
    
    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("file_tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))
    
    def test_new(self):
        new_base_model = BaseModel()
        new_user = User()
        new_state = State()
        new_place = Place()
        new_review = Review()
        new_amenity = Amenity()
        new_city = City()

        models.storage.new(new_base_model)
        models.storage.new(new_user)
        models.storage.new(new_state)
        models.storage.new(new_place)
        models.storage.new(new_city)
        models.storage.new(new_amenity)
        models.storage.new(new_review)

        self.assertIn("BaseModel." + new_base_model.id, models.storage.all().keys())
        self.assertIn(new_base_model, models.storage.all().values())
        self.assertIn("User." + new_user.id, models.storage.all().keys())
        self.assertIn(new_user, models.storage.all().values())
        self.assertIn("State." + new_state.id, models.storage.all().keys())
        self.assertIn(new_state, models.storage.all().values())
        self.assertIn("Place." + new_place.id, models.storage.all().keys())
        self.assertIn(new_place, models.storage.all().values())


if __name__ == "__main__":
    unittest.main()
