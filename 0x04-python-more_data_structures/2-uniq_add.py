#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = list()
    total = 0
    for i in my_list:
        if i not in new:
            total += i
            new.append(i)
    return total
