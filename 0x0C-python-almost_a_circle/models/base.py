#!/usr/bin/python3
"""

the first class base 
"""


class Base:
    """
    class base that is the principal class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        the constructor of the base class
        """

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

