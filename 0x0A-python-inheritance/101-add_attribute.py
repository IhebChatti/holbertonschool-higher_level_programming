#!/usr/bin/python3


def add_attribute(object, name, value):
    """add_attribute function

    Arguments:
        object {[object]} -- [object whose attribute has to be set]
        name {[str]} -- [attribute name]
        value {[str]} -- [value given to the attribute]

    Raises:
        TypeError: [if object cant have attribute]
    """
    if not hasattr(object, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(object, name, value)
