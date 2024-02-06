#!/usr/bin/python3
"""define json to object func"""
import json


def from_json_string(my_str):
    """retrurn python object represent"""
    return json.loads(my_str)
