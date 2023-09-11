#!/usr/bin/python3
""" Define the class Mylist """


class MyList(list):
    """ Here is the inheritence using Super """

    def print_sorted(self):
        print(sorted(self))
