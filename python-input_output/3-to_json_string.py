#!/usr/bin/python3
"""Write a function that returns the JSON representation of an object (string):
"""


def to_json_string(my_obj):
    """
    It converts a python object to a json string.

    :param my_obj: the object to be serialized
    """

    return json.dumps(my_obj)
