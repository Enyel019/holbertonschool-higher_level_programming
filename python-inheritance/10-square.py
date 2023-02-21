#!/usr/bin/python3
"""Importing the class Rectangle from the file 9-rectangle.py"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    rectangle class
    """

    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(self.__size, self.__size)

    def area(self):
        return self.__size * self.__size
