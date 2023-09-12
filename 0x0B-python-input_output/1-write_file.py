#!/usr/bin/python3
""" Defines the function write_file """


def write_file(filename="", text=""):
    """ Writes text int the tet=xt file and returns number of characters """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
