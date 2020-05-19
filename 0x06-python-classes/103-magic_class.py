#!/usr/bin/python3
import math
""" defining magic class """


class MagicClass:
    """ Magic Class """
    def __init__(self, radius=0):
        """ defining init
        args:
            radius """
        self.__radius = 0
        if type(radius) is not int or type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """ returns area of circle """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """ returns circumference of circle """
        return 2 * math.pi * self.__radius
