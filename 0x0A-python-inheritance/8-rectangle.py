#!/usr/bin/python3
"""class Rectangle that inherits from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class

    Arguments:
        BaseGeometry {[BaseGeomry]} -- [inherits from BaseGeometry]
    """
    def __init__(self, width, height):
        """Rectangle initiation

        Arguments:
            width {[int]} -- [width of rectangle]
            height {[int]} -- [height of rectangle]
        """
        self.integer_validator("height", height)
        self.__height = height
        self.integer_validator("width", width)
        self.__width = width
