#!/usr/bin/python3
import json
"""[creates an Object from a “JSON file”:]
"""


def load_from_json_file(filename):
    """[load_from_json_file]

    Arguments:
        filename {[str]} -- [the file name]

    Returns:
        [object] -- [json object]
    """
    with open(filename, encoding="utf-8") as myFile:
        return json.load(myFile)
