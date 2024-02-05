#!/usr/bin/python3
"""define basegeometry """


class BaseGeometry:
    """represent basegeomtry """
    def area(self):
        """not implemented """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """validate parameter as an int"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
