#!/usr/bin/python3
""" Write a function that adds 2 integers
"""


def add_integer(a, b=98):
    """
    Add_integer() adds two integers and returns the sum

    :param a: first integer
    :param b: 98, defaults to 98 (optional)
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
