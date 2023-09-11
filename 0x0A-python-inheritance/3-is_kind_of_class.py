#!/usr/bin/python3
""" Define the function is_kind_of_class """


def is_kind_of_class(obj, a_class):
    """ returns True if the object is an instance

    Attributes: obj, a_class)
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
