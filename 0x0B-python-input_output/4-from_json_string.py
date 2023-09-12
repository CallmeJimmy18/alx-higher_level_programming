#!/usr/bin/python3
""" Define the function from_json_string """
import json


def from_json_string(my_str):
    """ function returns an object represented by a JSON string """
    return json.loads(my_str)
