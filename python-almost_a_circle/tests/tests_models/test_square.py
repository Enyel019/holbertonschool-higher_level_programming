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

    def tearDown(self):
        """ deletes once proved"""
        if os.path.exists("Base.json"):
            os.remove("Base.json")
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.exists("Square.json"):
            os.remove("Square.json")


if __name__ == '__main__':
    unittest.main()
