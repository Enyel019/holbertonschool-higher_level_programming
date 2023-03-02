#!/usr/bin/python3
"""Write the first class Base:
"""
import json
import os


class Base:
    """
    It's a base class for all other classes.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """gets string"""
        if list_dictionaries is None or list_dictionaries is []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """write objects to file"""
        fn = cls.__name__ + ".json"
        nl = []
        if list_objs is not None:
            list_objs = [nl.append(i.to_dictionary()) for i in list_objs]
        with open(fn, "w", encoding="utf-8") as fl:
            fl.write(cls.to_json_string(nl))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """creates"""
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Square:
            dummy = cls(1)
        elif cls is Rectangle:
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy
