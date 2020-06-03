#!/usr/bin/python3
"""[from str to object]
"""
import json


def from_json_string(my_str):
    """from_json_string

    Arguments:
        my_str {[str]} -- [string]

    Returns:
        [object] -- [json object]
    """
    return json.loads(my_str)
