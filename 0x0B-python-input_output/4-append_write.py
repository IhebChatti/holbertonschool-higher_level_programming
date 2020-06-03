#!/usr/bin/python3
"""[append write file]
"""


def append_write(filename="", text=""):
    """append_write

    Keyword Arguments:
        filename {str} -- [the name of file] (default: {""})
        text {str} -- [the text to be appended] (default: {""})
    """
    with open(filename, mode="a", encoding="utf-8") as myFile:
        return myFile.write(text)
