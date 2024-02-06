#!/usr/bin/python3
"""define student class"""


class Student:
    """represent student """

    def __init__(self, first_name, last_name, age):
        """initialize new student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """dictionary represent of student"""
        return self.__dict__
