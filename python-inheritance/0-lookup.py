#!/usr/bin/python3
"""Write a function that returns the list of available
   attributes and methods of an object
   """


def lookup(obj):
    """
    It returns the list of valid attributes for the object.

    :param obj: The object to be looked up
    """
    l = []
    l = dir(obj)
    return l
