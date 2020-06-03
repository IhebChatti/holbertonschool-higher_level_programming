#!/usr/bin/python3
"""number of lines function
"""


def number_of_lines(filename=""):
    """number_of_lines

    Keyword Arguments:
        filename {str} -- [the file to get it's nmbr of lines] (default: {""})

    Returns:
        [int] -- [number of lines]
    """
    count = 0
    with open("my_file_0.txt", encoding="utf-8") as myFile:
        for line in myFile:
            count += 1
    return count
