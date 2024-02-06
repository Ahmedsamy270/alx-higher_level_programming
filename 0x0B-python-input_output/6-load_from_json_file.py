#!/usr/bin/python3
"""define json file reading func"""
import json


def load_from_json_file(filename):
    """creat python obj from json"""
    with open(filename) as f:
        return json.load(f)
