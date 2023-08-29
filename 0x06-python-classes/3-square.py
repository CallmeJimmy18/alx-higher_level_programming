#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represents a square"""
    def __init__(self, size=0):
        """Initialises a new Square

        Args:
            size (int): this is the size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self._size = size

        def area(self):
            return self._size ** 2
