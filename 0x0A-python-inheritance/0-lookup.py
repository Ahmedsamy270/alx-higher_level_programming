#!/usr/bin/python3
"""define object attribute lookup func"""


def lookup(obj):
    """return list of obects available attributes"""
    return (dir(obj))
