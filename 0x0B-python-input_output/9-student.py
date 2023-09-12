#!/usr/bin/python3
""" Define the class Student """


class Student:
    """ Represents a student """

    def __init__(self, first_name, last_name, age):
        """ Initializes the student class

        Args:
            first_name (str): the first name of the student
            last_name (str): this is the last name of the student
            age (int): the age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        def to_json(self):
            """ retrieves a dictionary representation of a Student """
            return self.__dict__
