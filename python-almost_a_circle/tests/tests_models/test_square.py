#!/usr/bin/python3

"""
square class set of unitestts
"""
import os
import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class SquareTest(unittest.TestCase):
    """especific square class tests"""

    def setUp(self):
        """set ups tests"""
        Base._Base__nb_objects = 0

    def test_docstring(self):
        """checks for docstring"""
        self.assertTrue(len(Square.__doc__) >= 1)

