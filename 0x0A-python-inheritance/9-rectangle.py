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

    def area(self):
        """ Returns the area of the rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ Return the print() and str() representation of a Rectangle """
        the_str = "[" + str(self.__class__.__name__) + "] "
        the_str += str(self.__width) + "/" + str(self.__height)
        return the_str
