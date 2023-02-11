#!/usr/bin/python3
"""Write a function that prints a square with the character #
"""


def print_square(size):
    """
    It prints a square of size n.

    :param size: the size of the square
    """
    msg_1 = "size must be an integer"
    msg_2 = "size must be >= 0"
    msg_3 = " size must be an integer"
    if not isinstance(size, int):
        raise TypeError(msg_1)
    if size < 0:
        raise TabError(msg_2)
    if isinstance(size, float) and size < 0:
        raise TypeError(msg_3)
    for squ in range(size):
        print('#' * size)
