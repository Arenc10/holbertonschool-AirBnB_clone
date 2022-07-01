#!/usr/bin/python3
"""Test module"""
import unittest
import models
from models.state import State
from datetime import datetime


class TestStateModel(unittest.TestCase):
    """Unittest for testing State class"""

    def test_no_args(self):
        self.assertEqual(State, type(State()))

    def test_id(self):
        self.assertEqual(str, type(State().id))

    def test_created_at(self):
        self.assertEqual(datetime, type(State().created_at))

    def test_updated_at(self):
        self.assertEqual(datetime, type(State().updated_at))
    
    def test_name(self):
        self.assertEqual(str, type(State().name))


if __name__ == "__main__":
    unittest.main()
