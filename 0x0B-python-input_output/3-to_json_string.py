#!/usr/bin/python3
"""define a string to json func"""
import json


def to_json_string(my_obj):
    """return json represent of a string object"""
    return json.dumps(my_obj)
