#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        x = my_list[0]
        for i in range(len(my_list)):
            if my_list[i] > x:
                x = my_list[i]
    else:
        return 'None'
    return x
