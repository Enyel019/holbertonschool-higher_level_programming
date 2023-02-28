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

    @property
    def width(self):
        return self.__wigth

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <=0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def heigth(self):
        return self.__heigth

    @heigth.setter
    def heigth(self, value):
        if type(value) is not int:
            raise TypeError('heigth must be an integer')
        if value <= 0:
            raise ValueError('heigth must be > o')
        self.__heigth = value


    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value
