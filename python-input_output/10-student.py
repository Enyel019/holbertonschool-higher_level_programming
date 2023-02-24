#!/usr/bin/python3
"""Write a class Student that defines a student by:
"""


class Student():

    def __init__(self, first_name, last_name, age):
        """
        This function takes in three parameters (first_name, last_name, age)
         and assigns them to the
        instance variables first_name, last_name, and age.

        :param first_name: The first name of the person
        :param last_name: The last name of the person
         :param age: The age of the person
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}
