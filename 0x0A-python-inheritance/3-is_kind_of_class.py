#!/usr/bin/python3
"""define a class and inherited class checking func"""


def is_kind_of_class(obj, a_class):
    """check if an object is instance or inherited of a class"""
    if isinstance(obj, a_class):
        return True
    return False
