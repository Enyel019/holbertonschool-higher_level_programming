#!/usr/bin/python3
"""Write a class BaseGeometry (based on 5-base_geometry.py).
"""


class BaseGeometry():
    """
    This class is a base class for all geometries

    """
    def area(self):
        raise Exception("area() is not implemen")

    def integer_validator(self, name, value):
        self.name = name
        self.value = value

        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value < 0 or value == 0:
            raise ValueError("{:s} must be greater than 0".format(name))
