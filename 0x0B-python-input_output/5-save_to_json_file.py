#!/usr/bin/python3
"""define json file writing func"""
import json


def save_to_json_file(my_obj, filename):
    """write an object to txt file using json"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
