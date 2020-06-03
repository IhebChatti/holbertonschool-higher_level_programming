#!/usr/bin/python3
"""function to read file
"""


def read_file(filename=""):
    """read_file function

    Keyword Arguments:
        filename {str} -- [the name of file to be read] (default: {""})
    """
    with open(filename, encoding="utf-8") as myFile:
        print(myFile.read(), end="")
