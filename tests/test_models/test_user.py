#!/usr/bin/python3
"""Test module"""
from models.user import User
import unittest
import models
from datetime import datetime


class TestUserModel(unittest.TestCase):
    """Unittest for testing User Class"""

    def test_no_args(self):
        self.assertEqual(User, type(User()))

    def test_id(self):
        self.assertEqual(str, type(User().id))

    def test_created_at(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_email(self):
        self.assertEqual(str, type(User().email))
    
    def test_password(self):
        self.assertEqual(str, type(User().password))
    
    def test_first_name(self):
        self.assertEqual(str, type(User().first_name))

    def test_last_name(self):
        self.assertEqual(str, type(User().last_name))


if __name__ == "__main__":
    unittest.main()
