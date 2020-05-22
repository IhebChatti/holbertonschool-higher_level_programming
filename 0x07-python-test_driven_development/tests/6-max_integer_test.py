#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        empty_list = []
        self.assertEqual(max_integer(empty_list), None)

    def test_max_at_start(self):
        max_list = [10, 6, 5, 2]
        self.assertEqual(max_integer(max_list), 10)

    def test_max_at_middle(self):
        max_list = [10, 9, 15, 4, 2]
        self.assertEqual(max_integer(max_list), 15)

    def test_max_negative(self):
        max_list = [-5, -10, -9, -1, -2]
        self.assertEqual(max_integer(max_list), -1)
    
    def test_strings_with_ints(self):
        max_list = ["hi", "hello", 5]
        with self.assertRaises(TypeError):
            max_integer(max_list)

    def  test_float_and_int(self):
        max_list = [3.4, 14, 66.66, 11]
        self.assertEqual(max_integer(max_list), 66.66)

    def test_floats_only(self):
        max_list = [1.1, 12.2, 14.5, 6.3]
        self.assertEqual(max_integer(max_list), 14.5)

    def test_strings_only(self):
        max_list = ["hi", "hello", "hello"]
        self.assertNotEqual(max_integer(max_list), "hello")

    def test_long_int(self):
        max_list = [111111111111111111111111111111111, 5, 2]
        self.assertEqual(max_integer(max_list), 111111111111111111111111111111111)

    def test_string(self):
        max_string = "hello"
        self.assertEqual(max_integer(max_string), 'o')

if __name__ == "__main__":
    unittest.main()