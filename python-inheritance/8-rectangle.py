#!/usr/bin/python3
"""Write a class BaseGeometry (based on 5-base_geometry.py).
"""


class BaseGeometry():
    """
    It's a class that defines a geometry.

    """
    def area(self):
        raise Exception("area() is not implemen")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value < 0 or value == 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Write a class Rectangle that inherits from
       BaseGeometry (7-base_geometry.py).
    """

    def __init__(self, width, height):
        self.__width = width
        self.__heigth = height
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
