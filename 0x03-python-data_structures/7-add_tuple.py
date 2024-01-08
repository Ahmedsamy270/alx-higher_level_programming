#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new = ()
    i = tuple_a + (0, 0)
    x = tuple_b + (0, 0)
    new = i[0] + x[0], i[1] + x[1]
    return new
