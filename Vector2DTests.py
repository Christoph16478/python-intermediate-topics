#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Test code.
"""

import unittest
import argparse

from classes.Vector2D import Vector2D

class Vector2DTests(unittest.TestCase):
    """class Vector2DTests
    """
    def setUp(self):
        self.vector_1 = Vector2D(0, 0)
        self.vector_2 = Vector2D(-1, 1)
        self.vector_3 = Vector2D(2.5, -2.5)

    def test_equality(self):
        """ Tests the equality operator.
        """
        self.assertNotEqual(self.vector_1, self.vector_2)
        expected_result = Vector2D(-1, 1)
        self.assertEqual(self.vector_2, expected_result)

    def test_add(self):
        """ Tests the addition operator.
        """
        result = self.vector_1 + self.vector_2
        expected_result = Vector2D(-1, 1)
        self.assertEqual(result, expected_result)

    def test_sub(self):
        """ Tests the subtraction operator.
        """
        result = self.vector_2 - self.vector_3
        expected_result = Vector2D(-3.5, 3.5)
        self.assertEqual(result, expected_result)

    def test_mul(self):
        """ Tests the multiplication operator.
        """
        result1 = self.vector_1 * 5
        expected_result1 = Vector2D(0.0, 0.0)
        self.assertEqual(result1, expected_result1)
        result2 = self.vector_1 * self.vector_2
        expected_result2 = 0.0
        self.assertEqual(result2, expected_result2)

    def test_div(self):
        """ Tests the multiplication operator.
        """
        result = self.vector_3 / 5
        expected_result = Vector2D(0.5, -0.5)
        self.assertEqual(result, expected_result)

def main():
    """main program
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--val1", help='first value (int)', type=int, required=True, dest='val1')
    parser.add_argument("--val2", help='first value (str)', type=str, required=True, dest='val2')
    parser.add_argument("--val3", help='first value (bool)', type=bool, required=True, dest='val3')
    args = parser.parse_args()
    print(args)
    a = args.val1
    b = args.val2
    c = args.val3
    print(a, type(a))
    print(b, type(b))
    print(c, type(c))

    vector_1 = Vector2D(2, -2)
    print(vector_1)
    vector_2 = Vector2D(2, 3)
    print(vector_2)
    vector_3 = vector_1 + vector_2
    print(vector_3)
    print("Hello world")

    unittest.main()

if __name__ == "__main__":
    main()
