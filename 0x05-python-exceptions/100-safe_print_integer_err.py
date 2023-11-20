#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print('{:d}'.format(value))
        return True
    except ValueError as msg:
        sys.stderr.write("Exception: " + str(msg) + "\n")
        return False
    except TypeError as msg:
        sys.stderr.write("Exception: " + str(msg) + "\n")
        return False
