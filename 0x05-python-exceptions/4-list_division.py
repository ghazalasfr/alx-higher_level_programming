#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list_N = []

    for i in range(list_length):
        try:
            list_N.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            list_N.append(0)
            print('division by 0')
            continue
        except IndexError:
            list_N.append(0)
            print('out of range')
            continue
        except TypeError:
            list_N.append(0)
            print('wrong type')
            continue
        finally:
            pass

    return list_N
