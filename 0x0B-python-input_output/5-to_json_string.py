#!/usr/bin/python3
"""[json representation of an obj]
"""
import json


def to_json_string(my_obj):
    """to_json_string

    Arguments:
        my_obj {[object]} -- [the object to get its representation]

    Returns:
        [str] -- [json representation of obj]
    """
    return json.dumps(my_obj)
