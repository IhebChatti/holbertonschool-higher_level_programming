#!/usr/bin/python3
"""Square definition
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square class

    Arguments:
        Rectangle {[Rectangle]} -- [inherits from Rectangle class]
    """
    def __init__(self, size):
        """square initialization

        Arguments:
            size {[int]} -- [size of square]
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """area

        Returns:
            [int] -- [area of square]
        """
        return self.__size ** 2
