#!/usr/bin/python3
"""
the square class with all property and functions
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    the def of square class that ihrets from rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        the def of init function
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        the str function
        """
        return '[Square] ({:d}) {:d}/{:d} - {:d}'.format(
            self.id, self.x, self.y, self.width
        )

    @property
    def size(self):
        """
        size function thatreturn size of square
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        the setter of size
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        the update function
        """
        argc = len(args)
        kwargc = len(kwargs)
        modif_attrs = ['id', 'size', 'x', 'y']

        if argc > 4:
            argc = 4

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
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
