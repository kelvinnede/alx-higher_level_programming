#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_positive_numbers(self):
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_mixed_numbers(self):
        result = max_integer([1, 3, 4, 2])
        self.assertEqual(result, 4)

    def test_negative_numbers(self):
        result = max_integer([-1, -2, -3, -4])
        self.assertEqual(result, -1)

    def test_empty_list(self):
        result = max_integer([])
        self.assertIsNone(result)

    def test_single_element_list(self):
        result = max_integer([5])
        self.assertEqual(result, 5)

    def test_duplicate_numbers(self):
        result = max_integer([5, 5, 5, 5])
        self.assertEqual(result, 5)

    def test_float_numbers(self):
        result = max_integer([1.5, 2.5, 3.5, 4.5])
        self.assertEqual(result, 4.5)

    def test_mixed_integer_and_float_numbers(self):
        result = max_integer([1, 2.5, 3, 4.5])
        self.assertEqual(result, 4.5)
