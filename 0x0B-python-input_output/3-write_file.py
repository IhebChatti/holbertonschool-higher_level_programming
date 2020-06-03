#!/usr/bin/python3
"""[write_file funection]
"""


def write_file(filename="", text=""):
    """write_file

    Keyword Arguments:
        filename {str} -- [name of the file] (default: {""})
        text {str} -- [description] (default: {""})

    Returns:
        [type] -- [description]
    """
    with open(filename, mode="w", encoding="utf-8") as myFile:
        return myFile.write(text)
