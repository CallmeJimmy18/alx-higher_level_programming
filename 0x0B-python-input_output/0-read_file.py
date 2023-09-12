#!/usr/bin/python3
""" Defines the function read_file """


def read_file(filename=""):
    """ prints the contents of the file """
    with open(filename, encoding="utf-8") as fle:
        fle_content = fle.read()
        print(fle_content, end="")
