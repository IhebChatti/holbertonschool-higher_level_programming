#!/usr/bin/python3
"""read_lines function
"""


def read_lines(filename="", nb_lines=0):
    """read_lines

    Keyword Arguments:
        filename {str} -- [name of file] (default: {""})
        nb_lines {int} -- [the number of lines] (default: {0})
    """
    with open("my_file_0.txt",  encoding="utf-8") as myFile:
        if nb_lines <= 0:
            print(myFile.read())
        else:
            for line in range(nb_lines):
                print(myFile.readline(), end="")
