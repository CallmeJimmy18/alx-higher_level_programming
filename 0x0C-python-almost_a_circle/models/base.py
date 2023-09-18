#!/usr/bin/python3
""" Defines the class base """
import json


class Base:
    """ Represents a base

    Attributes:
        __nb_objects (int): class attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initilizes the class Base

        Args:
            id (int): the instance id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Return the JSON string representation of list_dictionaries """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file """
        fle = cls.__name__ + ".json"
        with open(fle, "w") as jsonf:
            if list_objs is None:
                jsonf.write("[]")
            else:
                list_dict = [d.to_dictionary() for d in list_objs]
                jsonf.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation json_string

        Args:
            json_string (str): this is a JSON string representation
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set

        Args:
            dictionary (dict): Key/value pairs of the attribute initialised.
        """
        if cls.__name__ == "Rectangle":
            nw = cls(1, 1)
        else:
            nw = cls(1)
        nw.update(**dictionary)
        return nw

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """
        fle = cls.__name__ + ".json"
        try:
            with open(fle, "r") as jsonfle:
                list_dict = Base.from_json_string(jsonfle.read())
                return [cls.create(**o) for o in list_dict]
        except IOError:
            return []
