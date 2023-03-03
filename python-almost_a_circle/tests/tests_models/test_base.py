#!/usr/bin/python3
"""Base tests
"""
from models.base import Base
import unittest
import os


class BaseTest(unittest.TestCase):
    def setUp(self):
        """setting up for each test """
        Base._Base__nb_objects = 0

    def test_id(self):
        """ checks if correct id was generated"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 4)

    def test_any_docstring(self):
        """Checks for any docstring"""
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_custom_id(self):
        '''Test custom str id'''
        i = "Behemoth"
        b = Base(i)
        self.assertEqual(b.id, i)


if __name__ == '__main__':
    unittest.main()
