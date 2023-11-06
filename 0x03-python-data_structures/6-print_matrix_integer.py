#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for x in matrix:
            i = 1
            length = len(x)

            for y in x:
                if i == length:
                    print('{:d}'.format(y), end='')
                else:
                    print('{:d}'.format(y), end=' ')
                i += 1

            print()y
