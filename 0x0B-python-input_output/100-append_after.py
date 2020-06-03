#!/usr/bin/python3
"""[append_after function]
"""


def append_after(filename="", search_string="", new_string=""):
    """[append_after]

    Keyword Arguments:
        filename {str} -- [name of file] (default: {""})
        search_string {str} -- [string to be searched] (default: {""})
        new_string {str} -- [new string] (default: {""})
    """
    with open(filename, mode="r+", encoding="utf-8") as MyFile:
        txt = ""
        for i in MyFile:
            txt += i
            if search_string in i:
                txt += new_string
        MyFile.seek(0)
        for i in txt:
            MyFile.write(i)
