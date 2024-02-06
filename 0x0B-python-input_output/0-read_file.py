#!/usr/bin/python3
"""define txt file reading func"""


def read_file(filename=""):
    """printing the content of a utf8 txt file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
