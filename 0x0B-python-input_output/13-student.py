#!/usr/bin/python3
"""[Student class]
"""


class Student:
    """[Student class definition]
    """
    def __init__(self, first_name, last_name, age):
        """[Student initialization]

        Arguments:
            first_name {[str]} -- [first name]
            last_name {[str]} -- [last name]
            age {[int]} -- [age of student]
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """[to_json]

        Keyword Arguments:
            attrs {[str]} -- [the attributes] (default: {None})

        Returns:
            [dict] -- [dictionnairy of attributes]
        """
        if isinstance(attrs, list) and all(isinstance(i, str) for i in attrs):
            return {j: getattr(self, j) for j in attrs if hasattr(self, j)}
        return self.__dict__

    def reload_from_json(self, json):
        """[replaces all attributes of the Student instance]

        Arguments:
            json {[dict]} -- [dictionary]
        """
        for key, val in json.items():
            self.__dict__[key] = val
