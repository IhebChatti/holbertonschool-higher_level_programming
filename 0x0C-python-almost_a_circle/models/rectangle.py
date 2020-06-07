#!/usr/bin/python3
from models.base import Base
"""[Rectangle definition]
"""


class Rectangle(Base):
    """[Rectangle class]

    Args:
        Base ([class]): [base class that rectangle inherits from]
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """[Rectangle initialization]

        Args:
            width ([int]): [width of rectangle]
            height ([int]): [height of rectangle]
            x (int, optional): [x coordinates]. Defaults to 0.
            y (int, optional): [y coordinates]. Defaults to 0.
            id ([int], optional): [id of rectangle]. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """[width getter}
        Returns:
            [int] -- [returns the width]
        """
        return self.__width

    @width.setter
    def width(self, value):
        """[width setter]
        Arguments:
            value {[int]} -- [the value of width]
        Raises:
            TypeError: [if value is not an int]
            ValueError: [if value is negative]
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """[height getter}
        Returns:
            [int] -- [returns the height]
        """
        return self.__height

    @height.setter
    def height(self, value):
        """[height setter]
        Arguments:
            value {[int]} -- [the value of height]
        Raises:
            TypeError: [if height is not an int]
            ValueError: [if height is negative]
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """[x getter]

        Returns:
            [int]: [x coordinates]
        """
        return self.__x

    @x.setter
    def x(self, value):
        """[x getter]

        Args:
            value ([int]): [value assigned to x]

        Raises:
            TypeError: [if value is not integer]
            ValueError: [if value is negative]
        """
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """[y getter]

        Returns:
            [int]: [y coordinates]
        """
        return self.__y

    @y.setter
    def y(self, value):
        """[y setter]

        Args:
            value ([int]): [value assigned to y]

        Raises:
            TypeError: [if vlaue is not integer]
            ValueError: [if value negative]
        """
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """Area of Rectangle
        Returns:
            [int] -- [returns the area of rectangle]
        """
        return self.__width * self.__height

    def display(self):
        """prints the rectangle in "#"
        Returns:
            [str] -- [printes the rectangle in "#"]
        """
        rec = ""
        if self.__width == 0 or self.__height == 0:
            return rec
        for l in range(self.__y):
            rec += "\n"
        for k in range(self.__height):
            for i in range(self.__x):
                rec += " "
            for j in range(self.__width):
                rec += "#"
            rec += "\n"
        print(rec, end="")

    def __str__(self):
        """[str method]

        Returns:
            [str]: [update the __str__ method]
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """[update mehod]
        """
        attr = ["id", "width", "height", "x", "y"]
        if len(args) < 1 or not args:
            for k, v in kwargs.items():
                setattr(self, k, v)
        for i in range(len(args)):
            setattr(self, attr[i], args[i])

    def to_dictionary(self):
        """[to dict method]

        Returns:
            [dict]: [dict representation of rectangle]
        """
        return self.__dict__
