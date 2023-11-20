#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    nbre = 0

    try:
        for i in my_list:
            if nbre < x:
                print('{}'.format(my_list[nbre]), end='')
                nbre += 1

        print()
    except TypeError:
        pass
    finally:
        return nbre
