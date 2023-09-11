#!/usr/bin/python3
""" Define the function is_same_class """


def is_same_class(obj, a_class):
    """Checks if the obj is an instance of the class a_class"""
    if type(obj) == a_class:
        return True
