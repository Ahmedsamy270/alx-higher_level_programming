#!/usr/bin/python3
"""define file writing func"""


def write_file(filename="", text=""):
    """writing a string to utf8 txt file"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
