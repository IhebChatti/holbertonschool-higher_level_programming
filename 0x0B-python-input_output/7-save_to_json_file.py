#!/usr/bin/python3
import json
"""[writes an Object to a text file, using a JSON rep]
"""


def save_to_json_file(my_obj, filename):
    """save_to_json_file

    Arguments:
        my_obj {[object]} -- [json object]
        filename {[str]} -- [name of file]

    Returns:
        [txt] -- [text file]
    """
    with open(filename, mode="w", encoding="utf-8") as myFile:
        return json.dump(my_obj, myFile)
