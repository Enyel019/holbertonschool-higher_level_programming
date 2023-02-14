#!/usr/bin/python3
"""Write a class Rectangle that defines a rectangle by
"""


class Rectangle:
    """
    A rectangle has a width, a height, an area, and a perimeter.
    """
    msg_1 = "width must be an integer"
    msg_2 = "width must be >= 0"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError(msg_1)
        elif value < 0:
            raise ValueError(msg_2)
        else:
            self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError(msg_1)
        elif value < 0:
            raise ValueError(msg_2)
        else:
            self.__width = value
