#!/usr/bin/python3


def append_after(filename="", search_string="", new_string=""):
    with open(filename, mode="r+", encoding="utf-8") as MyFile:
        txt = ""
        for i in MyFile:
            txt += i
            if search_string in i:
                txt += new_string
        MyFile.seek(0)
        for i in txt:
            MyFile.write(i)