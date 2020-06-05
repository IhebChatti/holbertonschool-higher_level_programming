#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.width = value

    @property
    def height(self):
        """height getter
        Returns:
            [int] -- [returns the height]
        """
        return self.height

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
        self.height = value

    @property
    def x(self):
        """[x getter]

        Returns:
            [int]: [x]
        """
        return self.x

    @x.setter
    def x(self, value):
        """[x setter]

        Args:
            value ([int]): [x]
        """
        self.x = value

    @property
    def y(self):
        """[y getter]

        Returns:
            [int]: [y]
        """
        return self.y

    @y.setter
    def y(self, value):
        """[y setter]

        Args:
            value ([int]): [y]
        """
        self.y = value
