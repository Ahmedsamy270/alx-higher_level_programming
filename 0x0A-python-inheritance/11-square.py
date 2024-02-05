#!/usr/bin/python3
"""sefine rectangle subclass """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """represent square"""
    def __init__(self, size):
        """initialization new square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """method for area of square"""
        return self.__size ** 2

    def __str__(self):
        """return string represent of square"""
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
