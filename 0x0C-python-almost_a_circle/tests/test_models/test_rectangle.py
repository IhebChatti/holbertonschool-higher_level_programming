#!/usr/bin/python3
"""[TestRectangle]
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """[testRectangle]

    Args:
        unittest ([unitest]): [unit testing framework]
    """
    def test_typeError(self):
        """[test typeError]
        """
        with self.assertRaises(TypeError):
            Rectangle("hi", "bye")

    def test_one_arg(self):
        """[test one argument]
        """
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_instantiation(self):
        """[test instantiation]
        """
        a = Rectangle(1, 2)
        self.assertIsInstance(a, Rectangle)

    def test_valueError(self):
        """[test valueError]
        """
        with self.assertRaises(ValueError):
            Rectangle(0, 5)

    def test_id(self):
        """[test ID]
        """
        rec1 = Rectangle(1, 5)
        rec1.id = 5
        self.assertEqual(rec1.id, 5)

    def test_area(self):
        """[test Area]
        """
        rec1 = Rectangle(2, 2)
        self.assertEqual(rec1.area(), 4)

    def test_None(self):
        """[test None as param]
        """
        with self.assertRaises(TypeError):
            Rectangle(None)

    def test_multiple_recs(self):
        """[test multiple recs]
        """
        rec1 = Rectangle(1, 2)
        rec2 = Rectangle(3, 4)
        rec3 = Rectangle(5, 6)
        self.assertEqual(rec1.id, rec3.id - 2)

if __name__ == '__main__':
    unittest.main()
