#!/usr/bin/python3
"""Test cases for Square class."""

import unittest
import sys
import os
from io import StringIO
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from base import Base
from square import Square
from rectangle import Rectangle


class TestSquare(unittest.TestCase):
    """Test cases for the Square class."""

    def setUp(self):
        """Reset the nb_objects counter before each test."""
        Base._Base__nb_objects = 0

    def test_square_is_base(self):
        """Test that Square is an instance of Base."""
        s = Square(10)
        self.assertIsInstance(s, Base)

    def test_square_is_rectangle(self):
        """Test that Square is an instance of Rectangle."""
        s = Square(10)
        self.assertIsInstance(s, Rectangle)

    def test_no_args(self):
        """Test Square with no arguments."""
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg(self):
        """Test Square with one argument."""
        s1 = Square(10)
        s2 = Square(11)
        self.assertEqual(s1.id, s2.id - 1)

    def test_two_args(self):
        """Test Square with two arguments."""
        s1 = Square(10, 2)
        s2 = Square(2, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_three_args(self):
        """Test Square with three arguments."""
        s1 = Square(10, 2, 2)
        s2 = Square(2, 2, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_four_args(self):
        """Test Square with four arguments."""
        s = Square(10, 2, 2, 12)
        self.assertEqual(s.id, 12)

    def test_more_than_four_args(self):
        """Test Square with more than four arguments."""
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_size_private(self):
        """Test that size is private."""
        with self.assertRaises(AttributeError):
            print(Square(10, 2, 3, 4).__size)

    def test_size_getter(self):
        """Test size getter."""
        s = Square(5, 7, 7, 1)
        self.assertEqual(5, s.size)

    def test_size_setter(self):
        """Test size setter."""
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.size)

    def test_width_getter(self):
        """Test width getter."""
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.width)

    def test_height_getter(self):
        """Test height getter."""
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.height)

    def test_x_getter(self):
        """Test x getter."""
        s = Square(10, 5, 7, 1)
        self.assertEqual(5, s.x)

    def test_y_getter(self):
        """Test y getter."""
        s = Square(10, 5, 7, 1)
        self.assertEqual(7, s.y)

    def test_size_zero(self):
        """Test size with zero value."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

    def test_size_negative(self):
        """Test size with negative value."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1, 2)

    def test_x_negative(self):
        """Test x with negative value."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(5, -1, 0, 1)

    def test_y_negative(self):
        """Test y with negative value."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(5, 1, -1, 1)

    def test_size_typeerror(self):
        """Test size with invalid type."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid")

    def test_x_typeerror(self):
        """Test x with invalid type."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "invalid")

    def test_y_typeerror(self):
        """Test y with invalid type."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, "invalid")

    def test_size_float(self):
        """Test size with float value."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(5.5)

    def test_x_float(self):
        """Test x with float value."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, 3.5)

    def test_y_float(self):
        """Test y with float value."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, 4.5)

    def test_size_None(self):
        """Test size with None value."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_size_str(self):
        """Test size with string value."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("9")

    def test_size_list(self):
        """Test size with list value."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([1, 2, 3])

    def test_size_dict(self):
        """Test size with dictionary value."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"a": 1, "b": 2}, 2)

    def test_size_tuple(self):
        """Test size with tuple value."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((1, 2, 3), 2, 3)

    def test_size_frozenset(self):
        """Test size with frozenset value."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(frozenset({1, 2, 3, 1}))

    def test_size_range(self):
        """Test size with range value."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(range(5))

    def test_size_bytes(self):
        """Test size with bytes value."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(b'Python')

    def test_size_bytearray(self):
        """Test size with bytearray value."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(bytearray(b'abcdefg'))

    def test_size_memoryview(self):
        """Test size with memoryview value."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(memoryview(b'abcedfg'))

    def test_size_inf(self):
        """Test size with infinity value."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('inf'))

    def test_size_nan(self):
        """Test size with NaN value."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('nan'))

    def test_area_small(self):
        """Test area method with small value."""
        s = Square(2, 0, 0, 0)
        self.assertEqual(s.area(), 4)

    def test_area_large(self):
        """Test area method with large value."""
        s = Square(999999999999999, 0, 0, 1)
        self.assertEqual(s.area(), 999999999999999 ** 2)

    def test_area_changed_attributes(self):
        """Test area method after changing attributes."""
        s = Square(2, 10, 1, 1)
        s.size = 7
        self.assertEqual(s.area(), 49)

    def test_area_one_arg(self):
        """Test area method with one argument."""
        s = Square(2, 10, 1, 1)
        with self.assertRaises(TypeError):
            s.area(1)

    def test_display_size(self):
        """Test display method with size only."""
        s = Square(2, 0, 0, 9)
        captured_output = StringIO()
        sys.stdout = captured_output
        s.display()
        sys.stdout = sys.__stdout__
        self.assertEqual("##\n##\n", captured_output.getvalue())

    def test_display_size_x(self):
        """Test display method with size and x."""
        s = Square(3, 1, 0, 18)
        captured_output = StringIO()
        sys.stdout = captured_output
        s.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(" ###\n ###\n ###\n", captured_output.getvalue())

    def test_display_size_y(self):
        """Test display method with size and y."""
        s = Square(4, 0, 1, 9)
        captured_output = StringIO()
        sys.stdout = captured_output
        s.display()
        sys.stdout = sys.__stdout__
        display = "\n####\n####\n####\n####\n"
        self.assertEqual(display, captured_output.getvalue())

    def test_display_size_x_y(self):
        """Test display method with size, x, and y."""
        s = Square(2, 3, 2, 1)
        captured_output = StringIO()
        sys.stdout = captured_output
        s.display()
        sys.stdout = sys.__stdout__
        display = "\n\n   ##\n   ##\n"
        self.assertEqual(display, captured_output.getvalue())

    def test_display_one_arg(self):
        """Test display method with one argument."""
        s = Square(3, 4, 5, 2)
        with self.assertRaises(TypeError):
            s.display(1)

    def test_str_method_print_size(self):
        """Test __str__ method with size only."""
        s = Square(4)
        captured_output = StringIO()
        sys.stdout = captured_output
        print(s)
        sys.stdout = sys.__stdout__
        correct = f"[Square] ({s.id}) 0/0 - 4\n"
        self.assertEqual(correct, captured_output.getvalue())

    def test_str_method_size_x(self):
        """Test __str__ method with size and x."""
        s = Square(5, 5)
        correct = f"[Square] ({s.id}) 5/0 - 5"
        self.assertEqual(correct, str(s))

    def test_str_method_size_x_y(self):
        """Test __str__ method with size, x, and y."""
        s = Square(7, 4, 22)
        correct = f"[Square] ({s.id}) 4/22 - 7"
        self.assertEqual(correct, str(s))

    def test_str_method_size_x_y_id(self):
        """Test __str__ method with all arguments."""
        s = Square(15, 1, 2, 3)
        self.assertEqual("[Square] (3) 1/2 - 15", str(s))

    def test_str_method_changed_attributes(self):
        """Test __str__ method after changing attributes."""
        s = Square(7, 0, 0, [4])
        s.size = 15
        s.x = 8
        s.y = 10
        self.assertEqual("[Square] ([4]) 8/10 - 15", str(s))

    def test_str_method_one_arg(self):
        """Test __str__ method with one argument."""
        s = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            s.__str__(1)

    def test_update_args_zero(self):
        """Test update method with zero arguments."""
        s = Square(10, 10, 10, 10)
        s.update()
        self.assertEqual("[Square] (10) 10/10 - 10", str(s))

    def test_update_args_one(self):
        """Test update method with one argument."""
        s = Square(10, 10, 10, 10)
        s.update(89)
        self.assertEqual("[Square] (89) 10/10 - 10", str(s))

    def test_update_args_two(self):
        """Test update method with two arguments."""
        s = Square(10, 10, 10, 10)
        s.update(89, 2)
        self.assertEqual("[Square] (89) 10/10 - 2", str(s))

    def test_update_args_three(self):
        """Test update method with three arguments."""
        s = Square(10, 10, 10, 10)
        s.update(89, 2, 3)
        self.assertEqual("[Square] (89) 3/10 - 2", str(s))

    def test_update_args_four(self):
        """Test update method with four arguments."""
        s = Square(10, 10, 10, 10)
        s.update(89, 2, 3, 4)
        self.assertEqual("[Square] (89) 3/4 - 2", str(s))

    def test_update_args_more_than_four(self):
        """Test update method with more than four arguments."""
        s = Square(10, 10, 10, 10)
        s.update(89, 2, 3, 4, 5)
        self.assertEqual("[Square] (89) 3/4 - 2", str(s))

    def test_update_args_None_id(self):
        """Test update method with None id."""
        s = Square(10, 10, 10, 10)
        s.update(None)
        correct = f"[Square] ({s.id}) 10/10 - 10"
        self.assertEqual(correct, str(s))

    def test_update_args_None_id_and_more(self):
        """Test update method with None id and more args."""
        s = Square(10, 10, 10, 10)
        s.update(None, 4, 5)
        correct = f"[Square] ({s.id}) 5/10 - 4"
        self.assertEqual(correct, str(s))

    def test_update_args_invalid_size_type(self):
        """Test update method with invalid size type."""
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(89, "invalid")

    def test_update_args_size_zero(self):
        """Test update method with size zero."""
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(89, 0)

    def test_update_args_size_negative(self):
        """Test update method with negative size."""
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(89, -5)

    def test_update_args_invalid_x_type(self):
        """Test update method with invalid x type."""
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(89, 2, "invalid")

    def test_update_args_x_negative(self):
        """Test update method with negative x."""
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(89, 1, -6)

    def test_update_args_invalid_y_type(self):
        """Test update method with invalid y type."""
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(89, 2, 3, "invalid")

    def test_update_args_y_negative(self):
        """Test update method with negative y."""
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s.update(89, 1, 2, -6)

    def test_update_args_size_before_x(self):
        """Test update method with size before x error."""
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(89, "invalid", "invalid")

    def test_update_args_size_before_y(self):
        """Test update method with size before y error."""
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(89, "invalid", 1, "invalid")

    def test_update_kwargs_one(self):
        """Test update method with one keyword argument."""
        s = Square(10, 10, 10, 10)
        s.update(id=1)
        self.assertEqual("[Square] (1) 10/10 - 10", str(s))

    def test_update_kwargs_two(self):
        """Test update method with two keyword arguments."""
        s = Square(10, 10, 10, 10)
        s.update(size=1, id=2)
        self.assertEqual("[Square] (2) 10/10 - 1", str(s))

    def test_update_kwargs_three(self):
        """Test update method with three keyword arguments."""
        s = Square(10, 10, 10, 10)
        s.update(size=1, id=89, x=2)
        self.assertEqual("[Square] (89) 2/10 - 1", str(s))

    def test_update_kwargs_four(self):
        """Test update method with four keyword arguments."""
        s = Square(10, 10, 10, 10)
        s.update(id=89, x=1, y=3, size=4)
        self.assertEqual("[Square] (89) 1/3 - 4", str(s))

    def test_update_kwargs_None_id(self):
        """Test update method with None id as keyword argument."""
        s = Square(10, 10, 10, 10)
        s.update(id=None)
        correct = f"[Square] ({s.id}) 10/10 - 10"
        self.assertEqual(correct, str(s))

    def test_update_kwargs_None_id_and_more(self):
        """Test update method with None id and more keyword arguments."""
        s = Square(10, 10, 10, 10)
        s.update(id=None, size=7, x=9)
        correct = f"[Square] ({s.id}) 9/10 - 7"
        self.assertEqual(correct, str(s))

    def test_update_kwargs_invalid_size_type(self):
        """Test update method with invalid size type as keyword argument."""
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(size="invalid")

    def test_update_kwargs_size_zero(self):
        """Test update method with size zero as keyword argument."""
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(size=0)

    def test_update_kwargs_size_negative(self):
        """Test update method with negative size as keyword argument."""
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(size=-5)

    def test_update_kwargs_invalid_x_type(self):
        """Test update method with invalid x type as keyword argument."""
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(x="invalid")

    def test_update_kwargs_x_negative(self):
        """Test update method with negative x as keyword argument."""
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(x=-5)

    def test_update_kwargs_invalid_y_type(self):
        """Test update method with invalid y type as keyword argument."""
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(y="invalid")

    def test_update_kwargs_y_negative(self):
        """Test update method with negative y as keyword argument."""
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s.update(y=-5)

    def test_update_args_and_kwargs(self):
        """Test update method with both args and kwargs."""
        s = Square(10, 10, 10, 10)
        s.update(89, 2, size=4, y=6)
        self.assertEqual("[Square] (89) 10/10 - 2", str(s))

    def test_update_kwargs_wrong_keys(self):
        """Test update method with wrong keyword keys."""
        s = Square(10, 10, 10, 10)
        s.update(a=5, b=10)
        self.assertEqual("[Square] (10) 10/10 - 10", str(s))

    def test_update_kwargs_some_wrong_keys(self):
        """Test update method with some wrong keyword keys."""
        s = Square(10, 10, 10, 10)
        s.update(size=5, id=89, a=1, b=54)
        self.assertEqual("[Square] (89) 10/10 - 5", str(s))

    def test_to_dictionary_output(self):
        """Test to_dictionary method output."""
        s = Square(10, 2, 1, 1)
        correct = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertDictEqual(correct, s.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        """Test to_dictionary method doesn't change object."""
        s1 = Square(10, 2, 1, 2)
        s2 = Square(1, 1, 1, 1)
        s2.update(**s1.to_dictionary())
        self.assertNotEqual(s1, s2)

    def test_to_dictionary_arg(self):
        """Test to_dictionary method with argument."""
        s = Square(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            s.to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
