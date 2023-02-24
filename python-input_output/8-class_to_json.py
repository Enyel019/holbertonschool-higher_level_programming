#!/usr/bin/python3
"""Write a function that returns the dictionary description with simple
   data structure (list, dictionary, string, integer and boolean)
   for JSON serialization of an object:
"""


def class_to_json(obj):
    """
    It takes an object and returns a dictionary containing all of the object's attributes

    :param obj: The object to be serialized
    """
    return obj.__dict__
