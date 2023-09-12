#!/usr/bin/python3
""" Defines a function called load_from_json_file """
import json


def load_from_json_file(filename):
    """ the function creates an Object from a “JSON file" """
    with open(filename) as fle:
        return json.loads(fle)
