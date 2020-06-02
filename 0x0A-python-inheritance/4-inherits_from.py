#!/usr/bin/python3
"""check if obj inhertied directly of a class
"""


def inherits_from(obj, a_class):
    """inherits_from definition

    Arguments:
        obj {[object]} -- [the object to check]
        a_class {[class]} -- [the class]

    Returns:
        [bool] -- [true if inherited directly, false if not]
    """
    if issubclass(type(obj), a_class) and not type(obj) == a_class:
        return True
    return False
