#!/usr/bin/python3
"""Defines unittests for models/review.py.
Unittest classes:
    TestReview_instantiation
    TestReview_save
    TestReview_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.review import Review


class TestReview_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Review class."""

    def test_no_arguments(self):
        self.assertEqual(Review, type(Review()))

    def test_public_id_str(self):
        self.assertEqual(str, type(Review().id))

    def test_created_at_is_datetime(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at_is_datetime(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_new_instance_stored(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_text_str(self):
        self.assertEqual(str, type(Review().text))

    def test_place_id(self):
        self.assertEqual(str, type(Review().place_id))

    def test_user_id(self):
        self.assertEqual(str, type(Review().user_id))



if __name__ == "__main__":
    unittest.main()
