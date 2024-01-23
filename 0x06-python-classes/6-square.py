#!/usr/bin/python3
"""defining a class Square"""


class Square:
    """represent a Square"""

    def __init__(self, size=0, position=(0, 0)):
        """initializing a new Square

        args:
            size (int): the size of Square"""

        self.size = size
        self.position = position

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

    @property
    def position(self):
        """setting the square position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(number >= 0 for number in value) or
                not all(isinstance(number, int) for number in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """return the area of Square"""
        return (self.__size * self.__size)

    def my_print(self):
        """"""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for x in range(self.__position[0])]
            [print("#", end="") for y in range(self.__size)]
            print("")
