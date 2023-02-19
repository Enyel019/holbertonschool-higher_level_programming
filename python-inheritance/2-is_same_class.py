#!/usr/bin/python3
"""Write a function that returns True if the object is exactly an instance
of the specified class ; otherwise False.
"""


def is_same_class(obj, a_class):
    """
    It checks if the object is an instance of the class.

    :param obj: an object
    :param a_class: a class object
    """

    if type(obj) is a_class:
        return True
    else:
        return False
