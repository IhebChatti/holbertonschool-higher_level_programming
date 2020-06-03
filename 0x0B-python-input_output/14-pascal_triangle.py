#!/usr/bin/python3


def pascal_triangle(n):
    """[pascal triangle]

    Arguments:
        n {[int]} -- [pascal triangle numner]

    Returns:
        [list of lists] -- [list of lists of ints]
    """
    triangle = []
    if n <= 0:
        return []
    for i in range(n):
        row = [1]
        if triangle:
            lr = triangle[-1]
            row.extend([sum(j) for j in zip(lr, lr[1:])])
            row.append(1)
        triangle.append(row)
    return triangle
