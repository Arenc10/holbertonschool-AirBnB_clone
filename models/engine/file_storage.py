#!/usr/bin/python3
"""FileStorage class created
"""
import json
import os
from datetime import datetime
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place
from models.user import User
from models.state import State
from models.base_model import BaseModel


class FileStorage:
    """Class that serializes instances to a json file and vice versa
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Method that returns the dictionary objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """Method that sets in __objects the obj with key
        """
        FileStorage.__objects[type(obj).__name__ + "." + obj.id] = obj

    def save(self):
        """Serializes __objects to the JSON file
        """
        my_dict = {}
        for key in FileStorage.__objects:
            my_dict[key] = FileStorage.__objects[key].to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """Deserializes the json file to __objects
        """
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except Exception:
            pass
