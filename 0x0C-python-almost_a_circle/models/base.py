#!/usr/bin/python3
"""[Base Definition]
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """[to json string method]

        Args:
            list_dictionaries ([list of dicts]): [list of dictionnairies]

        Returns:
            [str]: [string representation of list of dicts]
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
