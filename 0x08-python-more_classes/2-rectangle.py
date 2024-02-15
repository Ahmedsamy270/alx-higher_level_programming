#!/usr/bin/python3
"""define the rectangle class """


class Rectangle:
    """this a class rectangle"""
    def __init__(self, width=0, height=0):
        """constractor initalzation """
        self.width = width
        self.height = height

    @property
    def height(self):
        """return height"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """return width"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """return rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """retutrn the rectangle perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return ((self.width + self.height) * 2)
