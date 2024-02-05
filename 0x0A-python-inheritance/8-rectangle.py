#!/usr/bin/python3
"""define class rectangle"""
BAseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle using basegeometry"""
    def __init__(self, width, height):
        """initialize new rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
