#!/usr/bin/python3
"""class to check if obj is an instance of a class
"""


def is_same_class(obj, a_class):
    """is_same_class definition

    Arguments:
        obj {[object]} -- [the object to check]
        a_class {[class]} -- [the class to check if obj is instance]

    Returns:
        [bool] -- [true if instance, false if not instance]
    """
    if type(obj) is a_class:
        return True
    return False
