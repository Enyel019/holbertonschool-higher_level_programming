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

    def area(self):
        return (self.__size * self.__size)

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        p = '#'
        c = self.__size
        if self.__size == 0:
            print()
        else:
            while(c):
                print("{}".format(p) * self.__size)
                c -= 1
