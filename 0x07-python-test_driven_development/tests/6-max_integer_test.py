#!/usr/bin/python3
"""finding max int in list"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_ordered_list(self):
        order = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unorderd(self):
        not_order = [1, 2, 4, 5]
        self.assertEqual(max_integer(not_order), 4)
    
    def test_max_at_begginning(self):
        max_at_beginning = [4, 1, 2, 3]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_empty_list(self):
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_el(self):
        oneel = [7]
        self.assertEqual(max_integer(oneel), 7)

    def test_floats(self):
        floats = [1.4, 6.2, -9.123, 10.2, 6.0]
        self.assertEqual(max_integer(floats), 10.2)

    def test_floats_and_int(self):
        floats_ints = [1.4, 6, -9.123, 10, 6.0]
        self.assertEqual(max_integer(floats_ints), 10)


    def test_string(self):
        string = "Garnet"
        self.assertEqual(max_integer(string), 'r')

    def test_strings_list(self):
        """Test a list of strings."""
        strings = ["Garnet", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
