#!/usr/bin/python3
"""
the rectangle class that ihrets from base
"""

from models.base import Base


class Rectangle(Base):
    """
    the main class of rectangle 
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        the init / constructor of the rectangle class
        """
        super().__init__(id)

        self.check_integer(width, 'width')
        self.check_integer(height, 'height')
        self.check_integer(x, 'x')
        self.check_integer(y, 'y')

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        witdh of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, val):
        """
        the setter of width
        """
        self.check_integer(val, 'width')

        self.__width = val

    @property
    def height(self):
        """
        the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, val):
        """
        setter of height
        """
        self.check_integer(val, 'height')

        self.__height = val

    @property
    def x(self):
        """
        property x
        """
        return self.__x

    @x.setter
    def x(self, val):
        """
        setter of x
        """
        self.check_integer(val, 'x')

        self.__x = val

    @property
    def y(self):
        """
        property y
        """
        return self.__y

    @y.setter
    def y(self, val):
        """
        setter of y
        """
        self.check_integer(val, 'y')

        self.__y = val

    def check_integer(self, value, val):
        """
        the function that check if the value is integer or not
        """
        if type(value) is not int:
            raise TypeError(val + ' must be an integer')

        if value <= 0 and val in ('width', 'height'):
            raise ValueError(val + ' must be > 0')

        if value < 0 and val in ('x', 'y'):
            raise ValueError(val + ' must be >= 0')

    def area(self):
        """
        the area function that return with*height 
        """
        return self.__width * self.__height

    def display(self):
        """
        display function that print the result
        """
        if self.__y > 0:
            print('\n' * self.__y, end='')

        for i in range(self.height):
            if self.__x > 0:
                print(' ' * self.__x, end='')

            print('#' * self.__width)

    def __str__(self):
        """
        the str function
        """
        return '[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}'.format(
            self.id, self.x, self.y, self.width, self.height
        )

    def update(self, *args, **kwargs):
        """
        the update function that make updates of all args
        """
        argc = len(args)
        kwargc = len(kwargs)
        modif_attrs = ['id', 'width', 'height', 'x', 'y']

        if argc > 5:
            argc = 5

        if argc > 0:
            for i in range(argc):
                setattr(self, modif_attrs[i], args[i])
        elif kwargc > 0:
            for k, v in kwargs.items():
                if k in modif_attrs:
                    setattr(self, k, v)

    def to_dictionary(self):
        """
        to dictionary function
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
