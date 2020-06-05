#!/usr/bin/python3
"""[Base Definition]
"""


class Base:
    """[Base class]
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """[Base initialization]

        Args:
            id ([int], optional): [the id]. Defaults to None.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
