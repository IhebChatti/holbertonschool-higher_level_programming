#!/usr/bin/python3
"""check if obj isan instance of a class
"""


def is_kind_of_class(obj, a_class):
    """is_kind_of_class definition

    Arguments:
        obj {[obj]} -- [the obj to check]
        a_class {[class]} -- [a_class]

    Returns:
        [bool] -- [true if isinstance, false if not]
    """
    if isinstance(obj, a_class):
        return True
    return False
