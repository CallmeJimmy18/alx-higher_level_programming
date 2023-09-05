#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for ch in text:
        print("{}".format(ch), end="")
        if (ch == '.' or ch == ',' or ch == '?' or ch == ':'):
            print("")
            print("")
