#!/usr/bin/python3
"""
Class Rectange
"""
from models.base import Base


class Rectangle(Base):
    '''class Rectangle
    manager inherits
    from Base'''
    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width setter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """rectangle area"""
        return self.width * self.height

    def display(self):
        """prints rectangle"""
        for h in range(self.y):
            print()
        for i in range(self.height):
            for w in range(self.x):
                print(" ", end="")
            print("#" * self.width)

    def __str__(self):
        """string info"""
        s1 = "[Rectangle] ({}) {}/{}".format(self.id, self.x, self.y)
        s2 = " - {}/{}".format(self.width, self.height)
        return s1 + s2

    def update(self, *args, **kwargs):
        """rectangle updater"""
        la = ['id', 'width', 'height', 'x', 'y']
        if args is not None and len(args) != 0:
            for b in range(len(args)):
                setattr(self, la[b], args[b])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """gets dictionary"""
        return{"id": self.id, "width": self.width, "height": self.height,
               "x": self.x, "y": self.y}
