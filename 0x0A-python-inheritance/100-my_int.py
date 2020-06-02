#!usr/bin/python3
"""MyInt rebel class
"""


class MyInt(int):
    """MyInt definition inherits from int

    Arguments:
        int {[object]} -- [int object]
    """
    def __eq__(self, number):
        """eq method but rebel one it is actually NE

        Arguments:
            number {[int]} -- [number to check]

        Returns:
            [int] -- [number]
        """
        return self.real != number

    def __ne__(self, number):
        """ne method but rebel one it is actually EQ

        Arguments:
            number {[int]} -- [number to check]

        Returns:
            [int] -- [number]
        """
        return self.real == number
