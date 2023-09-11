#!/usr/bin/python3
""" Define function inherits_from """


def inherits_from(obj, a_class):
    """ Looks if obj is an insatnce of the a class inherited

    Args:
        obj: the object checked
        a_class: this is the class inherited

    Return: True or False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
