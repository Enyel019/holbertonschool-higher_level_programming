#!/usr/bin/python3
"""Write a function that returns an object (Python data structure)
   represented by a JSON string:
"""

import json


def from_json_string(my_str):
    """
    It converts a string to a JSON object.

    :param my_str: a string representing a JSON object
    """

    return json.loads(my_str)
