#!/usr/bin/python3
"""define a class checking func """


def is_same_class(obj, a_class):
    """check if an object is exactly an instance"""
    if type(obj) == a_class:
        return True
    return False
