#!/usr/bin/python3
""" Define the function class_to_json """


def class_to_json(obj):
    """ this funct returns the dictionary description """
    return obj.__dict__
