#!/usr/bin/python3
"""Write a class Square that defines a square by
"""


class Square:
    """It creates a class called Square.
    """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
