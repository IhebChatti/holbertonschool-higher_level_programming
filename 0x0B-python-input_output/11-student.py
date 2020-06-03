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

    def to_json(self):
        """[to json method]

        Returns:
            [dict] -- [dictionnairy holding the description of object]
        """
        return self.__dict__
