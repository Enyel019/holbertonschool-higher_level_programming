#!/usr/bin/python3
"""Base tests
"""
from models.rectangle import Rectangle
from models.base import Base
import unittest
import os


class RectangleTest(unittest.TestCase):
    """The `BaseTest` class is a subclass of the `unittest.TestCase` class
    """


def setUp(self):
    """setting up for each test """
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


if __name__ == '__main__':
    unittest.main()
