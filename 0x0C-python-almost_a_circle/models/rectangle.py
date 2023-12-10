#!/usr/bin/python3
"""
the rectangle class with all function
"""

from models.base import Base


class Rectangle(Base):
    """
    rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        the constructor of rectangle class
        """
        super().__init__(id)

        self.check_function(width, 'width')
        self.check_function(height, 'height')
        self.check_function(x, 'x')
        self.check_function(y, 'y')

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        width function that return width
        """
        return self.__width

    @width.setter
    def width(self, newval):
        """
        setter of width that set the width to new value
        """
        self.check_function(newval, 'width')

        self.__width = newval

    @property
    def height(self):
        """
        heisght function
        """
        return self.__height

    @height.setter
    def height(self, newval):
        """
        setter of height
        """
        self.check_function(newval, 'height')

        self.__height = newval

    @property
    def x(self):
        """
        the x parameter
        """
        return self.__x

    @x.setter
    def x(self, newX):
        """
        setter of x 
        """
        self.check_function(newX, 'x')

        self.__x = newX

    @property
    def y(self):
        """
        the y parameter
        """
        return self.__y

    @y.setter
    def y(self, newY):
        """
        setter of y
        """
        self.check_function(newY, 'y')

        self.__y = param
 def check_function(self, value, newValue):
        """
        ...
        """
        if type(value) is not int:
            raise TypeError(newValue + ' must be an integer')

        if value <= 0 and newValue in ('width', 'height'):
            raise ValueError(newValue + ' must be > 0')

        if value < 0 and newValue in ('x', 'y'):
            raise ValueError(newValue + ' must be >= 0')
