#!/usr/bin/python3

"""
Write a function that writes a string to a text file (UTF8) and returns the number of characters written:
"""

def number_of_lines(filename=""):
    """
    the function define that return nulber of caracter
    """

    with open(filename, encoding='utf-8') as f:
        """
        the open function that used it to open the file
        """

        return len(f.readlines())
