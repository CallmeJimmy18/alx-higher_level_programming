#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represents a square"""
    def __init__(self, size=0):
        """Initialises a new Square

        Args:
            size (int): this is the size of the square
        """
        self.size = size

    @property
    def size(self):
        """Gets the current size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be an integer")
        self.__size = value

    def area(self):
        """This is the squared area of the square"""
        return self.__size * self.__size
