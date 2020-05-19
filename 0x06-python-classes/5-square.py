#!/usr/bin/python3
""" Defining a Square """


class Square:
    def __init__(self, size=0):
        """ Initializing a Square
        args:
            size: size of square """
        self.size = size

    @property
    def size(self):
        """ getter def """
        return self.__size

    @size.setter
    def size(self, value):
        """ size setting
        args:
            value: new value of size """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    """ area method """
    def area(self):
        return self.size ** 2

    def my_print(self):
        if self.size == 0:
            print()
        for i in range(self.size):
            for j in range(self.size):
                print('#', end='')
            print()
