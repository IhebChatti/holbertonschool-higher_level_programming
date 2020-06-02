#!/usr/bin/python3
"""function that returns the list of available
attributes and methods of an object
"""


def lookup(obj):
    """lookup definition

    Arguments:
        obj {[object]} -- [the object to get attributes and methods]

    Returns:
        [list] -- [list of attr and methods]
    """
    return dir(obj)
