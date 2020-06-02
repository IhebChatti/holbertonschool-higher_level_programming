#!/usr/bin/python3
"""a class that inherits from list
"""


class MyList(list):
    """My list definition

    Arguments:
        list {[list]} -- [list]
    """
    def print_sorted(self):
        """prints a sorted list
        """
        print(sorted(self))
