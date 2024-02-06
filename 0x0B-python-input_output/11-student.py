#!/usr/bin/python3
"""define student class"""


class Student:
    """represent student """

    def __init__(self, first_name, last_name, age):
        """initialize new student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """dictionary represent of student"""
        if (type(attrs) == list and all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """replace all attribute of student"""
        for k, v in json.items():
            setattr(self, k, v)
