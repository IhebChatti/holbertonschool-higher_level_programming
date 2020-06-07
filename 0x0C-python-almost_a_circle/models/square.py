#!/usr/bin/python3
from models.rectangle import Rectangle
"""[Square Definition]
"""


class Square(Rectangle):
    """[square class]

    Args:
        Rectangle ([class]): [class that square inherits from]
    """

    def __init__(self, size, x=0, y=0, id=None):
        """[square initialization]

        Args:
            size ([int]): [size of square]
            x (int, optional): [x coordinates]. Defaults to 0.
            y (int, optional): [y coordinates]. Defaults to 0.
            id ([type], optional): [square id]. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """[size getter]

        Returns:
            [int]: [size of square]
        """
        return self.width

    @size.setter
    def size(self, value):
        """[size setter]

        Args:
            value ([int]): [value assigned to size]
        """
        self.width = value
        self.height = value

    def __str__(self):
        """[str method]

        Returns:
            [str]: [str representation of square]
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.size)

    def update(self, *args, **kwargs):
        """[update mehod]
        """
        attr = ["id", "size", "x", "y"]
        if len(args) < 1 or not args:
            for k, v in kwargs.items():
                setattr(self, k, v)
        for i in range(len(args)):
            setattr(self, attr[i], args[i])

    def to_dictionary(self):
        """[to dict method]

        Returns:
            [dict]: [dict representaiton of square]
        """
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
