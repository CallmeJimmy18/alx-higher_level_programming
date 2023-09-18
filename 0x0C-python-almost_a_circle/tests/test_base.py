#!/usr/bin/python3
""" Define the test case for Base class """
import sys
import json
import unittest
from models.base import Base
from io import StringIO
from models.rectangle import Rectangle
from models.square import Square


class Test_Base_case(unittest.TestCase):
    """ This is the class for the Base TestCase """

    def test_no_args(self):
        """ Tests if id is correct with no arguments """
        b = Base()
        b2 = Base()
        self.assertEqual(b.id, b2.id - 1)

    def test_with_args(self):
        """ Tests if id is correct with an argument """
        b = Base(5)
        b2 = Base(12)
        self.assertEqual(b.id, 5)
        self.assertEqual(b2.id, 12)

    def test_float_id(self):
        """ Tests when the id is a float """
        b = Base(5.5)
        self.assertEqual(b.id, 5.5)

    def test_public_id(self):
        """ Test the id when it is reassigned """
        b = Base(12)
        b.id = 17
        self.assertEqual(b.id, 17)

    def test_two_args(self):
        """ Test is the exception is raised when two args """
        with self.assertRaises(TypeError):
            Base(2, 4)

    def test_with_negative_arg(self):
        """ Test if user types in negative id argument """
        nb = Base(-3)
        self.assertEqual(nb.id, -3)

    def test_json_string_empty_list(self):
        """ Test if json string saved to empty list """
        res = Base.to_json_string([])
        self.assertEqual(res, "[]")

    def test_json_string_list_dict(self):
        """ test the list of dict is not empty list """
        th_list = [{"id": 10,
                    "width": 5,
                    "height": 10,
                    "x": 0,
                    "y": 0
                    }]
        res = Base.to_json_string(th_list)
        expect = json.dumps(th_list)
        self.assertEqual(res, expect)

    def test_to_json_string_none(self):
        """ tests if the list is none """
        self.assertEqual("[]", Base.to_json_string(None))


class Testing_Base_save_file(unittest.TestCase):
    """ Test the file save for the base class """

    def removes(self):
        """ Removes all created files """
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_save_to_none(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as fle:
            self.assertEqual("[]", fle.read())

    def test_create_obj(self):
        """ Testing the new object creation """
        r = Rectangle(10, 6, 2, 3, 7)
        r_dictionary = r.to_dictionary()
        r2 = Rectangle.create(**r_dictionary)
        self.assertNotEqual(r, r2)

    def test_create_with_dictionary(self):
        obj_dict = {'id': 1, 'width': 2, 'height': 3, 'x': 4, 'y': 5}
        obj = Rectangle.create(**obj_dict)

        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.width, 2)
        self.assertEqual(obj.height, 3)
        self.assertEqual(obj.x, 4)
        self.assertEqual(obj.y, 5)

    def test_create_with_default_values(self):
        obj_dict = {}
        obj = Rectangle.create(**obj_dict)

        self.assertEqual(obj.id, 4)
        self.assertEqual(obj.width, 1)
        self.assertEqual(obj.height, 1)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)

    def test_create_with_partial_attributes(self):
        obj_dict = {'id': 1, 'width': 2}
        obj = Rectangle.create(**obj_dict)

        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.width, 2)
        self.assertEqual(obj.height, 1)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)

    def test_load_from_file_rectangle(self):
        r_1 = Rectangle(10, 7, 2, 8, 1)
        r_2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r_1, r_2])
        list_rectanglesoutput = Rectangle.load_from_file()
        self.assertEqual(str(list_rectanglesoutput[0]), str(r_1))

    def test_load_from_file_square(self):
        s_1 = Square(5, 1, 3, 3)
        s_2 = Square(9, 5, 2, 3)
        Square.save_to_file([s_1, s_2])
        squares_output = Square.load_from_file()
        self.assertEqual(str(squares_output[0]), str(s_1))


if __name__ == '__main__':
    unittest.main()
