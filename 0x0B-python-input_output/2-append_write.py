#!/usr/bin/python3
"""define  file append func"""


def append_write(filename="", text=""):
    """append a string to the end of txt file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
