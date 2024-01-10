#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = list()
    tmp = set(my_list)
    total = 0
    for i in tmp:
        total += i
    new.append(total)
    return new
