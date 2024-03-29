#!/usr/bin/python3
"""defining a class Square"""


class Square:
    """represent a Square"""

    def __init__(self, size=0):
        """initializing a new Square

        args:
            size (int): the size of Square"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
