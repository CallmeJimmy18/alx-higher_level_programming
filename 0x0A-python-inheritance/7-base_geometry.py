#!/usr/bin/python3
""" Define an empty class """


class BaseGeometry:
    """ BaseGeometry class """
    def area(self):
        """Area method raises exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ integer_validator method validates the value """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
