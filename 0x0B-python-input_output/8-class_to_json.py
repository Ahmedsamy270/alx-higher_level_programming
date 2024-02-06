#!/usr/bin/python3
"""define python class to json func"""


def class_to_json(obj):
    """return a dictionary represent"""
    return obj.__dict__
