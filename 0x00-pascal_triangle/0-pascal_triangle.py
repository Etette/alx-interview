#!/usr/bin/python3
"""
0-Pascal_triangle.py: pascal_trinangle()
"""

def pascal_triangle(n=9):
    """
    returns a list of lists of integers.
    Args:
        n (int) number of lists and digits
    returns: list of lists
    """
    i = [1]
    j = [0]
    listOfLists = []

    if n <= 0:
        return listOfLists

    for num in range(n):
        listOfLists.append(i)
        i = [l+r for l, r in zip(i + j, j + i)]
    return listOfLists
