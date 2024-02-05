#!/usr/bin/python3
"""contain all mylist class """


class MyList(list):
    """ the subclass of list"""
    def __init__(self):
        """ initalze object"""
        super().__init__()

    def print_sorted(self):
        """print sorted list """
        print(sorted(self))
