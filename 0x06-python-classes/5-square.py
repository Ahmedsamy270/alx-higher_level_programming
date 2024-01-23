#!/usr/bin/python3
"""defining a class Square"""


class Square:
    """represent a Square"""

    def __init__(self, size=0):
        """initializing a new Square

        args:
            size (int): the size of Square"""

        self.size = size

    @property
    def size(self):
        """setting the square size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return the area of Square"""
        return (self.__size * self.__size)

    def my_print(self):
        """"""
        for i in range(self.__size):
            [print("#", end="") for x in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
