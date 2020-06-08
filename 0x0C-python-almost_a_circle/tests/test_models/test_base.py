#!/usr/bin/python3
import unittest
from models.base import Base
"""[test_base]
"""


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


if __name__ == '__main__':
    unittest.main()
