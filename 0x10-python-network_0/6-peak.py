#!/usr/bin/python3
"""[python script to find peak of list]
"""


def peakfinder(list_of_integers, bot, top):
    """[recursively search for peak in list]

    Args:
        list_of_integers ([list]): [list of ints]
        bot ([int]): [first item of list]
        top ([int]): [last item of list]

    Returns:
        [int]: [peak of list]
    """
    if bot == top:
        return list_of_integers[top]
    mid = (bot + top) // 2
    if list_of_integers[mid + 1] < list_of_integers[mid]:
        return peakfinder(list_of_integers, bot, mid)
    return peakfinder(list_of_integers, mid + 1, top)


def find_peak(list_of_integers):
    """[find peak function]

    Args:
        list_of_integers ([list]): [list containing ints]
    """
    n = len(list_of_integers)
    if n == 0:
        return None
    if n == 1:
        return list_of_integers[0]
    return peakfinder(list_of_integers, 0, n - 1)
