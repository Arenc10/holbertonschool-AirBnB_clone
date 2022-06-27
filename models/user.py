#!/usr/bin/python3
"""
Defines a User model
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
