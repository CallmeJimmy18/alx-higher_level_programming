#!/usr/bin/python3
""" Define a Square class that inherits from the class Rectangle """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Represents a square """

    def __init__(self, size):
        """ Initialize a new square

        Args:
            size: the size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
