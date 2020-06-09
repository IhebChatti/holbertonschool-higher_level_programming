#!/usr/bin/python3
"""[unit testing square]
"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """[TestSquare]

    Args:
        unittest ([unittest]): [unit testing framework]
    """
    def test_instantiation(self):
        """[test_instantiation]
        """
        s = Square(1)
        self.assertIsInstance(s, Square)

    def test_TypeError(self):
        """[test_TypeError]
        """
        with self.assertRaises(TypeError):
            Square("Hello")

    def test_ValueError(self):
        """[test_ValueError]
        """
        with self.assertRaises(ValueError):
            Square(-5)

    def test_id(self):
        """[test_id]
        """
        s1 = Square(1, 5)
        s1.id = 5
        self.assertEqual(s1.id, 5)

    def test_area(self):
        """[test Area]
        """
        s1 = Square(2, 2)
        self.assertEqual(s1.area(), 4)

    def test_multiple_Squares(self):
        """[test_multiple_squares]
        """
        s1 = Square(4)
        s2 = Square(5)
        s3 = Square(6)
        self.assertEqual(s1.id, s3.id - 2)

    def test_None(self):
        """[test None as param]
        """
        with self.assertRaises(TypeError):
            s1 = Square(None)

if __name__ == '__main__':
    unittest.main()
