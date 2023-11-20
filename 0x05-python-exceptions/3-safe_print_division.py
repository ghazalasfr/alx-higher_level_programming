#!/usr/bin/python3
def safe_print_division(a, b):
    nbre = 0

    try:
        nbre = a / b
    except ZeroDivisionError:
        nbre = None
    finally:
        print('Inside result: {}'.format(nbre))
        return nbre
