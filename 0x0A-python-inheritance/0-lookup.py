#!/usr/bin/python3
""" Define function lookup """


def lookup(obj):
    """Return a list of an object's available attributes."""
    return (dir(obj))
