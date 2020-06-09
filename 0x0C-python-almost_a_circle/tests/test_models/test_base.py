#!/usr/bin/python3
"""[test_base]
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """[test_base]

    Args:
        unittest ([unittest]): [unit testing framework]
    """
    def test_args(self):
        """[test args]
        """
        base = Base()
        self.assertEqual(base.id, 1)

    def test_multiple_bases(self):
        """[test_multple_bases]
        """
        base1 = Base()
        base2 = Base()
        base3 = Base()
        base4 = Base()
        self.assertEqual(base1.id, base4.id - 3)

    def test_id(self):
        """[test_id]
        """
        base1 = Base(15)
        base1.id = 5
        self.assertEqual(5, base1.id)

    def test_none(self):
        """[test None as arg]
        """
        base1 = Base(None)
        base2 = Base(None)
        base3 = Base(None)
        self.assertEqual(base1.id, base3.id - 2)

    def test_to_json_string(self):
        """[test_to_json_string]
        """
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(type(json_dictionary), str)

    def test_from_json_string(self):
        """[test_from_json_string]
        """
        list_input = [{'id': 89, 'width': 10, 'height': 4},
                      {'id': 7, 'width': 1, 'height': 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(type(list_output), list)

    def test_create(self):
        """[test_create]
        """
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(r1 is r2, False)

if __name__ == '__main__':
    unittest.main()
