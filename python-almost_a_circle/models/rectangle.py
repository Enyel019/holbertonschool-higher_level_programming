#!/usr/bin/python3
"""Write the class Rectangle that inherits from Base:
"""
from models.base import Base


class Rectangle(Base):
    """
    A rectangle is a shape with a width and a height.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.heigth = height
        self.x = x
        self.y = y
        super().__init__(id)

