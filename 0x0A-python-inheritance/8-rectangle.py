#!/usr/bin/python3
""" Define a Rectangle class inherited from BaseGeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Represents a reactangle using BaseGeometry """

    def __init__(self, width, height):
        """ Initializes a rectangle class

        Args:
            width: the width of the new rectangle
            height: the height of the new rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
