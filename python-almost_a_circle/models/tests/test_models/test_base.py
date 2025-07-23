#!/usr/bin/python3
"""Test cases for Base class."""

import unittest
import os
import json
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from base import Base
from rectangle import Rectangle
from square import Square


class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def setUp(self):
        """Reset the nb_objects counter before each test."""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Clean up files after tests."""
        files = ["Base.json", "Rectangle.json", "Square.json"]
        for file in files:
            if os.path.exists(file):
                os.remove(file)

    def test_id_with_argument(self):
        """Test Base with id argument."""
        b1 = Base(12)
        self.assertEqual(b1.id, 12)

    def test_id_without_argument(self):
        """Test Base without id argument."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_id_none(self):
        """Test Base with None id."""
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_id_mixed(self):
        """Test Base with mixed id types."""
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 12)
        self.assertEqual(b3.id, 2)

    def test_nb_objects_private(self):
        """Test that nb_objects is private."""
        b1 = Base()
        with self.assertRaises(AttributeError):
            print(b1.nb_objects)

    def test_to_json_string_empty_list(self):
        """Test to_json_string with empty list."""
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

    def test_to_json_string_none(self):
        """Test to_json_string with None."""
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_to_json_string_rectangle(self):
        """Test to_json_string with Rectangle dictionary."""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_string = Base.to_json_string([dictionary])
        self.assertIsInstance(json_string, str)
        self.assertIn("10", json_string)
        self.assertIn("7", json_string)

    def test_to_json_string_square(self):
        """Test to_json_string with Square dictionary."""
        s1 = Square(10, 2, 3)
        dictionary = s1.to_dictionary()
        json_string = Base.to_json_string([dictionary])
        self.assertIsInstance(json_string, str)
        self.assertIn("10", json_string)

    def test_from_json_string_empty_string(self):
        """Test from_json_string with empty string."""
        list_output = Base.from_json_string("")
        self.assertEqual(list_output, [])

    def test_from_json_string_none(self):
        """Test from_json_string with None."""
        list_output = Base.from_json_string(None)
        self.assertEqual(list_output, [])

    def test_from_json_string_valid_json(self):
        """Test from_json_string with valid JSON."""
        list_input = [{"id": 89, "width": 10, "height": 4}]
        json_string = Base.to_json_string(list_input)
        list_output = Base.from_json_string(json_string)
        self.assertEqual(list_output, list_input)

    def test_save_to_file_none(self):
        """Test save_to_file with None."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            content = f.read()
        self.assertEqual(content, "[]")

    def test_save_to_file_empty_list(self):
        """Test save_to_file with empty list."""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            content = f.read()
        self.assertEqual(content, "[]")

    def test_save_to_file_rectangle(self):
        """Test save_to_file with Rectangle instances."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            content = f.read()
        self.assertIsInstance(content, str)
        self.assertIn("10", content)
        self.assertIn("7", content)

    def test_save_to_file_square(self):
        """Test save_to_file with Square instances."""
        s1 = Square(10, 7, 2)
        s2 = Square(2)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as f:
            content = f.read()
        self.assertIsInstance(content, str)
        self.assertIn("10", content)

    def test_load_from_file_no_file(self):
        """Test load_from_file when file doesn't exist."""
        list_rectangles = Rectangle.load_from_file()
        self.assertEqual(list_rectangles, [])

    def test_load_from_file_rectangle(self):
        """Test load_from_file with Rectangle."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()

        self.assertEqual(len(list_rectangles_output), 2)
        self.assertEqual(list_rectangles_output[0].width, 10)
        self.assertEqual(list_rectangles_output[0].height, 7)
        self.assertEqual(list_rectangles_output[1].width, 2)
        self.assertEqual(list_rectangles_output[1].height, 4)

    def test_load_from_file_square(self):
        """Test load_from_file with Square."""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()

        self.assertEqual(len(list_squares_output), 2)
        self.assertEqual(list_squares_output[0].size, 5)
        self.assertEqual(list_squares_output[1].size, 7)

    def test_create_rectangle(self):
        """Test create method with Rectangle."""
        r1 = Rectangle(3, 5, 1, 0, 99)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)

        self.assertEqual(r1.width, r2.width)
        self.assertEqual(r1.height, r2.height)
        self.assertEqual(r1.x, r2.x)
        self.assertEqual(r1.y, r2.y)
        self.assertEqual(r1.id, r2.id)
        self.assertIsNot(r1, r2)

    def test_create_square(self):
        """Test create method with Square."""
        s1 = Square(3, 5, 1, 99)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)

        self.assertEqual(s1.size, s2.size)
        self.assertEqual(s1.x, s2.x)
        self.assertEqual(s1.y, s2.y)
        self.assertEqual(s1.id, s2.id)
        self.assertIsNot(s1, s2)

    def test_update_rectangle(self):
        """Test update method with Rectangle."""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=1)
        self.assertEqual(r1.height, 1)

        r1.update(width=1, x=2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.x, 2)

        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r1.y, 1)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.id, 89)

    def test_update_square(self):
        """Test update method with Square."""
        s1 = Square(5)
        s1.update(size=10)
        self.assertEqual(s1.size, 10)

        s1.update(size=1, x=2)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 2)


if __name__ == "__main__":
    unittest.main()
