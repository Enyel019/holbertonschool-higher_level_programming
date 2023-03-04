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

    def test_isinstance(self):
        '''It tests whether an object is an instance of a class'''
        r = Rectangle(1, 2)
        self.assertEqual(isinstance(r, Base), True)

    def test_class(self):
        '''Testsclass'''
        self.assertEqual(str(Rectangle),
                         "<class 'models.rectangle.Rectangle'>")


if __name__ == '__main__':
    unittest.main()
