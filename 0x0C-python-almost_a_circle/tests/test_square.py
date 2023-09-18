#!/usr/bin/python3
""" Test the the square class """
import unittest
import sys
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_base(unittest.TestCase):

    def setUp(self):
        self.stdout_backup = sys.stdout
        sys.stdout = StringIO()

    def teardown(self):
        sys.stdout = self.stdout_backup

    def test_is_base(self):
        self.assertIsInstance(Square(10), Base)

    def test_if_one_arg(self):
        s1 = Square(10)
        s2 = Square(11)
        self.assertEqual(s1.id, s2.id - 1)

    def test_constructor(self):
        s1 = Square(10, 20, 2, 100)
        self.assertEqual(s1.id, 100)
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.x, 20)
        self.assertEqual(s1.y, 2)

    def getter_and_setter(self):
        s2 = Square(10, 10, 10, 10)
        s2.size = 3
        s2.x = 3
        s2.y = 3
        self.assertEqual(s2.id, 10)
        self.assertEqual(s2.size, 3)
        self.assertEqual(s2.x, 3)
        self.assertEqual(s2.y, 3)

    def test_Square_with_some_args(self):
        s4 = Square(3, 3, 1)
        s5 = Square(3, 2)
        s4.id = 10
        s5.id = 10
        self.assertEqual(s4.id, 10)
        self.assertEqual(s5.id, 10)
        self.assertEqual(s5.y, 0)

    def test_size_non_integer(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s3 = Square("r", 1, 2, 50)

    def test_size_non_integer_setter(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s3 = Square(3, 1, 2, 50)
            s3.size = "j"

    def test_size_eqauls_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s3 = Square(0, 1, 2, 50)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s3 = Square(7, 1, 2, 50)
            s3.size = 0

    def test_size_smaller_than_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s3 = Square(-9, 1, 2, 50)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s3 = Square(7, 1, 2, 50)
            s3.size = -6

    def test_x_eqauls_zero(self):
        s3 = Square(7, 0, 2, 50)
        self.assertEqual(s3.x, 0)

    def test_y_eqauls_zero(self):
        s3 = Square(7, 3, 0, 50)
        self.assertEqual(s3.y, 0)

    def test_x_smaller_than_zero(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s3 = Square(9, -1, 2, 50)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s3 = Square(7, 1, 2, 50)
            s3.x = -6

    def test_y_smaller_than_zero(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s3 = Square(6, 1, -2, 50)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s3 = Square(7, 1, 2, 50)
            s3.y = -2

    def test_x_non_integer(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s3 = Square(5, [5], 2, 50)

    def test_x_non_integer_setter(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s3 = Square(3, 1, 2, 50)
            s3.y = "J"

    def test_normal_area(self):
        s4 = Square(3)
        self.assertEqual(s4.area(), 9)

    def test_area_modification(self):
        s6 = Square(99)
        s6.size = 4
        self.assertEqual(s6.area(), 16)

    def test_normal_area(self):
        s7 = Square(2)
        s7.display()
        outed = sys.stdout.getvalue()
        expect = "##\n##\n"
        self.assertEqual(outed, expect)

    def test_area_is_one(self):
        s7 = Square(1)
        s7.display()
        outed = sys.stdout.getvalue()
        expect = "#\n"
        self.assertEqual(outed, expect)

    def test_normal_offset(self):
        s7 = Square(2, 1, 1)
        s7.display()
        outed = sys.stdout.getvalue()
        expect = "\n ##\n ##\n"
        self.assertEqual(outed, expect)

    def test_zero_offset(self):
        s7 = Square(2, 0, 0)
        s7.display()
        outed = sys.stdout.getvalue()
        expect = "##\n##\n"
        self.assertEqual(outed, expect)

    def test_no_yoffset(self):
        s7 = Square(2, 2)
        s7.display()
        outed = sys.stdout.getvalue()
        expect = "  ##\n  ##\n"
        self.assertEqual(outed, expect)

    def test_no_offset(self):
        s7 = Square(2)
        s7.display()
        outed = sys.stdout.getvalue()
        expect = "##\n##\n"
        self.assertEqual(outed, expect)

    def test_normal_Square_using_string(self):
        s8 = Square(4, 7, 2, 3)
        self.assertEqual(str(s8), "[Square] (3) 7/2 - 4")

    def test_normal_Square_using_print(self):
        s8 = Square(4, 7, 2, 3)
        print(s8)
        outed = sys.stdout.getvalue()
        expect = "[Square] (3) 7/2 - 4\n"
        self.assertEqual(outed, expect)

    def test_print_width_and_height_of_one(self):
        s8 = Square(1, 0, 0, 0)
        self.assertEqual(str(s8), "[Square] (0) 0/0 - 1")

    def test_print_no_x_y_or_id(self):
        s8 = Square(1)
        self.assertEqual(str(s8), "[Square] ({}) 0/0 - 1". format(s8.id))

    def test_some_args(self):
        s7 = Square(1, 2, 3)
        s6 = Square(1, 2)
        s8 = Square(1)
        self.assertEqual(str(s7), "[Square] ({}) 2/3 - 1". format(s7.id))
        self.assertEqual(str(s6), "[Square] ({}) 2/0 - 1". format(s6.id))
        self.assertEqual(str(s8), "[Square] ({}) 0/0 - 1". format(s8.id))

    def test_normal_update_using_args(self):
        s1 = Square(1, 3, 5, 7)
        s1.update(6, 8, 2, 10)
        self.assertEqual(str(s1), "[Square] (6) 2/10 - 8")

    def test_modify_after_update(self):
        s1 = Square(1, 3, 5, 7)
        s1.update(6, 8, 2, 10)
        s1.id = 200
        self.assertEqual(str(s1), "[Square] (200) 2/10 - 8")

    def test_update_somw_args(self):
        s1 = Square(1, 3, 5, 7)
        s2 = Square(1, 3, 5, 7)
        s3 = Square(1, 3, 5, 7)
        s1.update(4, 4, 4)
        s2.update(3, 3)
        s3.update(1)
        self.assertEqual(str(s1), "[Square] (4) 4/5 - 4")
        self.assertEqual(str(s2), "[Square] (3) 3/5 - 3")
        self.assertEqual(str(s3), "[Square] (1) 3/5 - 1")

    def test_no_args(self):
        r1 = Square(6, 8, 9, 10)
        r1.update()
        self.assertEqual(str(r1), "[Square] (10) 8/9 - 6")

    def test_extra_args(self):
        r1 = Square(6, 8, 9, 10)
        r1.update(5, 5, 5, 5, 5, 5, 5)
        self.assertEqual(str(r1), "[Square] (5) 5/5 - 5")

    def test_non_integrs(self):
        r2 = Square(5, 8, 4, 8)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r2.update(6, "", 8, 8)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r2.update(6, 8, {}, 9)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r2.update(6, 6, 8, [7])

    def test_smaller_than_zero(self):
        r2 = Square(5, 8, 4, 8)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r2.update(6, -34, 8, 8)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r2.update(6, 8, -78, 9)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r2.update(6, 6, 8, -1)

    def test_equals_zero(self):
        r2 = Square(5, 8, 4, 8)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r2.update(6, 0, 8, 8)

    def test_None(self):
        r2 = Square(5, 8, 4, 8)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r2.update(6, None, 8, 8)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r2.update(6, 8, None, 9)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r2.update(6, 6, 8, None)

    def test_normal_update_using_kwargs(self):
        r1 = Square(1, 3, 5, 7)
        r1.update(id=6, size=7, x=2, y=10)
        self.assertEqual(str(r1), "[Square] (6) 2/10 - 7")

    def test_unordered_arguments(self):
        s1 = Square(1, 3, 5, 7)
        s1.update(id=6, size=7, y=2, x=10)
        self.assertEqual(str(s1), "[Square] (6) 10/2 - 7")

    def test_update_some_kwargs(self):
        s1 = Square(1, 3, 5, 7)
        s2 = Square(1, 3, 5, 7)
        s3 = Square(1, 3, 5, 7)
        s1.update(id=4, size=4, x=4)
        s2.update(id=3, size=3)
        s3.update(id=1,)
        self.assertEqual(str(s1), "[Square] (4) 4/5 - 4")
        self.assertEqual(str(s2), "[Square] (3) 3/5 - 3")
        self.assertEqual(str(s3), "[Square] (1) 3/5 - 1")

    def test_update_id_kwarg(self):
        r1 = Square(6, 8, 9, 10)
        r1.update(id=4)
        self.assertEqual(r1.id, 4)

    def test_extra_args(self):
        r1 = Square(6, 8, 9, 10)
        r1.update(id=5, width=5, size=5, y=5, x=5, height=5, jam=5, update=5)
        self.assertEqual(str(r1), "[Square] (5) 5/5 - 5")

    def test_non_integrs(self):
        r2 = Square(5, 8, 4, 8)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r2.update(id=6, size="", x=8, y=9)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r2.update(id=6, size=8, x={}, y=9)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r2.update(id=6, size=6, x=8, y=[7])

    def test_smaller_than_zero(self):
        r2 = Square(5, 8, 4, 8)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r2.update(id=6, size=-34, x=8, y=9)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r2.update(id=6, size=8, x=-78, y=9)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r2.update(id=6, size=6, x=8, y=-1)

    def test_equals_zero(self):
        r2 = Square(5, 8, 4, 8)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r2.update(id=6, size=0, x=8, y=9)

    def test_None_as_arg(self):
        r2 = Square(5, 8, 4, 8)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r2.update(id=6, size=None, x=8, y=9)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r2.update(id=6, size=8, x=None, y=9)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r2.update(id=6, size=6, x=8, y=None)

    def test_dictionary_normal(self):
        r2 = Square(10, 2, 1, 1)
        expect = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertDictEqual(r2.to_dictionary(), expect)

    def test_dictionary_new_obj(self):
        r1 = Square(10, 2, 1, 1)
        r2 = Square(10, 2, 1, 1)
        expect = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertDictEqual(r2.to_dictionary(), expect)

    def test_dictionary_normal(self):
        r2 = Square(10, 2, 1)
        expect = {'id': r2.id, 'x': 2, 'size': 10, 'y': 1}
        self.assertDictEqual(r2.to_dictionary(), expect)
