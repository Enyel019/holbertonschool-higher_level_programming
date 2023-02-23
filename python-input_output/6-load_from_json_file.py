#!/udr/bin/python3
"""Write a function that creates an Object from a “JSON file”:
"""
import json


def load_from_json_file(filename):
    """
    It creates an object from a JSON file.

    :param filename: the name of the file to load from
    """

    with open(filename, "r") as file:
        return json.load(file)
