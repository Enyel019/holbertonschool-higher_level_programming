#!/usr/bin/python3

"""set of tests rectangle class"""

import unittest
from models.rectangle import Rectangle
from models.base import Base
import os


class RectangleTest(unittest.TestCase):
    """Tests rectangle class"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_docstring(self):
        """checks for any docstring"""
        self.assertTrue(len(Rectangle.__doc__) >= 1)

    def tearDown(self):
        if os.path.exists("Base.json"):
            os.remove("Base.json")
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_class(self):
        '''Testsclass'''
        self.assertEqual(str(Rectangle),
                         "<class 'models.rectangle.Rectangle'>")
