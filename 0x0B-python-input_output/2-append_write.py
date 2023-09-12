#!/usr/bin/python3
""" Defines the function append_write """


def append_write(filename="", text=""):
    """ This function appends the file

    Arg:
        filename (str): This is the name of the file
        text (str): THis is the text to be appened

    Return: the number of characters added
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
