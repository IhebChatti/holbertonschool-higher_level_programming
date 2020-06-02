#!/usr/bin/python3
"""class BaseGeometry
"""


class BaseGeometry:
    """BaseGeometry definition
    """

    def area(self):
        """area not implemented

        Raises:
            Exception: [area is not implemented yet]
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """integer_validator definition

        Arguments:
            name {[string]} -- [the name]
            value {[int]} -- [value]

        Raises:
            TypeError: [if value is not an integer]
            ValueError: [if value <= 0]
        """
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
