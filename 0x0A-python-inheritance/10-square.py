#!/usr/bin/python3
"""sefine rectangle subclass """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """represent square"""
    def __init__(self, size):
        """initialization new square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
