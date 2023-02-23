#!/usr/bin/python3
"""Write a function that writes an Object to a text file,
   using a JSON representation:
"""
import json


def save_to_json_file(my_obj, filename):
    """
    It writes an object to a text file using a JSON representation.

    :param my_obj: the object to be serialized
    :param filename: the name of the file to write to
    """

    with open(filename, "w", encoding="utf-8") as file:
        file.write(json.dumps(my_obj))
