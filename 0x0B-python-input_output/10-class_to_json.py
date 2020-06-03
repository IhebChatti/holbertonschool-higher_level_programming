#!/usr/bin/python3
"""[returns the dictionary description with simple data structure]
"""


def class_to_json(obj):
    """[class_to_json gives the description with simple data struc]

    Arguments:
        obj {[object]} -- [the object to check]

    Returns:
        [dict] -- [dictionnairy holding the descrip of simple data struct]
    """
    return obj.__dict__
