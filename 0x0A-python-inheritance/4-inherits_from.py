#!/usr/bin/python3
"""define an inherited class func"""


def inherits_from(obj, a_class):
    """check if an object is an inherited instance of aclass"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
