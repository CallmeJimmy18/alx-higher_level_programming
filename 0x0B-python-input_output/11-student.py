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
            """ retrieves a dictionary representation of a Student

            Args:
                attrs (list): The attributes to represent.
            """
            if (type(attrs) == list and
                    all(type(element) == str for ele in attrs)):
                return {j: getattr(self, j) for j in attrs if hasattr(self, j)}
            return self.__dict__

        def reload_from_json(self, json):
            """ replaces all attributes of the Student instance

            Args:
                json : Values to replace attributs with
            """
            for key, val in json.items():
                setattr(self, key, val)
