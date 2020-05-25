#!/usr/bin/python3
"""Defining a rectangle
"""


class Rectangle:
    """Rectangle
    """
    def __init__(self, width=0, height=0):
        """initializing a Rectangle

        Keyword Arguments:
            width {int} -- [width of rectangle] (default: {0})
            height {int} -- [height of rectangle] (default: {0})
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """width getter

        Returns:
            [int] -- [returns the width]
        """
        return self.__width

    @width.setter
    def width(self, value):
        """width setter

        Arguments:
            value {[int]} -- [the value of width]

        Raises:
            TypeError: [if value is not an int]
            ValueError: [if value is negative]
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """height getter

        Returns:
            [int] -- [returns the height]
        """
        return self.__height

    @height.setter
    def height(self, value):
        """height setter

        Arguments:
            value {[int]} -- [the value of height]

        Raises:
            TypeError: [if height is not an int]
            ValueError: [if height is negative]
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Area of Rectangle

        Returns:
            [int] -- [returns the area of rectangle]
        """
        return self.width * self.height

    def perimeter(self):
        """Perimeter of Rectangle

        Returns:
            [int] -- [retunrs the perimeter of rectangle]
        """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.height + self.width) * 2

    def __str__(self):
        """prints the rectangle in "#"

        Returns:
            [str] -- [printes the rectangle in "#"]
        """
        rec = ""
        for i in range(self.height):
            for j in range(self.width):
                rec += "#"
            if i + 1 < self.height:
                rec += "\n"
        if self.width == 0 or self.height == 0:
            rec = ""
        return rec

    def __repr__(self):
        """representation of rectangle

        Returns:
            [] -- [representation or rectangle]
        """
        return 'Rectangle''({}, {})'.format(self.width, self.height)

    def __del__(self):
        """prints a message when instance is deleted
        """
        print('Bye rectangle...')
