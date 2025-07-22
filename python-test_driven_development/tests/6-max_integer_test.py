#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_ordered_list(self):
        """Test an ordered list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test a list with a max value at the beginning"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        """Test a list with a max value in the middle"""
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)

    def test_one_element(self):
        """Test a list with only one element"""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test an empty list"""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Test a list with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_positive_negative(self):
        """Test a list with positive and negative numbers"""
        self.assertEqual(max_integer([-5, -1, 3, -10]), 3)

    def test_all_same_values(self):
        """Test a list where all elements are the same"""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_float_numbers(self):
        """Test a list with float numbers"""
        self.assertEqual(max_integer([1.5, 2.7, 3.1, 2.9]), 3.1)

    def test_large_numbers(self):
        """Test a list with large numbers"""
        self.assertEqual(max_integer([1000000, 999999, 1000001]), 1000001)

    def test_zero_in_list(self):
        """Test a list containing zero"""
        self.assertEqual(max_integer([0, -1, -2]), 0)
        self.assertEqual(max_integer([0, 1, 2]), 2)

    def test_duplicate_max_values(self):
        """Test a list with duplicate maximum values"""
        self.assertEqual(max_integer([3, 5, 5, 2]), 5)

    def test_single_negative(self):
        """Test a list with single negative number"""
        self.assertEqual(max_integer([-42]), -42)

    def test_two_elements(self):
        """Test a list with two elements"""
        self.assertEqual(max_integer([1, 2]), 2)
        self.assertEqual(max_integer([2, 1]), 2)

    def test_very_long_list(self):
        """Test a very long list"""
        long_list = list(range(1000))
        self.assertEqual(max_integer(long_list), 999)

    def test_default_parameter(self):
        """Test function called without parameters
           (uses default empty list)"""
        self.assertIsNone(max_integer())


if __name__ == '__main__':
    unittest.main()
