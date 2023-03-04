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


def test_any_docstring(self):
    """Checks for any docstring"""
    self.assertTrue(len(Base.__doc__) >= 1)


def test_isinstance(self):
    r = Rectangle(1, 2)
    self.assertEqual(isinstance(r, Rectangle), True)
