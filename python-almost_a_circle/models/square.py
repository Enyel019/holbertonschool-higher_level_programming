#!/usr/bin/python3
"""Write the class Square that inherits from Rectangle:
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A Square is a Rectangle with equal width and height.
    """

    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        st1 = "[Square] ({}) {}/{}".format(self.id, self.x, self.y)
        st2 = " - {}".format(self.size)
        return st1 + st2

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
