#!/usr/bin/python3
"""
Defines a base model
"""
from datetime import datetime
import uuid
import models


class BaseModel:
    """ Base class
    """

    def __init__(self):
        """__init__ - initalizes the base class

        Args:
            id (str): uuid of the object converted to a string
            created_at (datetime): Time when instance is created
            updated_at (datetime): Time when instance is updated
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Str representation of classs
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ Updates the public instance attribute wit the current daytime
        """
        self.updated_at = datetime.now()
        return self.updated_at

    def to_dict(self):
        """Returns a dictionary containing all keys/values of dict
        """
        my_dict = self.__dict__
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
