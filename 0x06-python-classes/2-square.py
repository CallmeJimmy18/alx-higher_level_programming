#!/usr/bin/python3
"""Define a the class Square"""


class Square:
    """Represents a square"""
    def __init__(self, size=0):
        """New Square initialised

            Args:
                size (int): This size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self._size = size
