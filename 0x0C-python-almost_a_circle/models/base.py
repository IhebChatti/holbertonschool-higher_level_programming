#!/usr/bin/python3
"""[Base Definition]
"""
import json
import csv
from os import path


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

    @classmethod
    def save_to_file(cls, list_objs):
        """[save_to_file static mehtod]

        Args:
            list_objs ([list of objs]): [list of objs]
        """
        my_list = []
        with open(cls.__name__ + ".json", mode="w") as MyFile:
            if list_objs is None:
                MyFile.write(Base.to_json_string([]))
            for obj in list_objs:
                my_list.append(obj.to_dictionary())
            MyFile.write(Base.to_json_string(my_list))

    @staticmethod
    def from_json_string(json_string):
        """[from_json_string method]

        Args:
            json_string ([json_string]): [json string]

        Returns:
            [list]: [list of json string representation]
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """[create class method]

        Returns:
            [instance of obj]: [instance of all attributes already set]
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
            dummy.update(**dictionary)
        if cls.__name__ == "Square":
            dummy = cls(1)
            dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """[load from file method]

        Returns:
            [list]: [list of instances]
        """
        if path.exists("{}.json".format(cls.__name__)) is False:
            return []
        with open(cls.__name__ + ".json", mode="r") as MyFile:
            my_list = cls.from_json_string(MyFile.read())
            return [cls.create(**items) for items in my_list]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """[save to csv file method]

        Args:
            list_objs ([list]): [list of objs]
        """
        with open(cls.__name__ + ".csv", mode="w") as MyFile:
            if list_objs is None:
                MyFile.write("[]")
            if cls.__name__ == "Rectangle":
                fnames = ["id", "width", "height", "x", "y"]
            elif cls.__name__ == "Square":
                fnames = ["id", "size", "x", "y"]
            spamwriter = csv.DictWriter(MyFile, fieldnames=fnames)
            spamwriter.writeheader()
            for i in list_objs:
                spamwriter.writerow(i.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """[load from csv file method]

        Returns:
            [lsit]: [list of objects]
        """
        if path.exists("{}.csv".format(cls.__name__)) is False:
            return []
        with open(cls.__name__ + ".csv", mode="r") as MyFile:
            my_list = []
            spamreader = csv.DictReader(MyFile)
            for _dict in spamreader:
                for key, val in _dict.items():
                    _dict[key] = int(val)
                my_list.append(cls.create(**_dict))
            return my_list
