#!/usr/bin/python3
"""Write a function that prints
"""


def say_my_name(first_name, last_name=""):
    """
    It prints out the first and last name of the person.

    :param first_name: a string
    :param last_name: This is a parameter with a default value.
    If we call the function without passing
    a value for last_name, it will default to the empty string
    """
    msg_1 = "first_name must be a string"
    msg_2 = "last_name must be a string"
    if not isinstance(first_name, str):
        raise TypeError(msg_1)
    if not isinstance(last_name, str):
        raise TypeError(msg_2)
    print("My name is {:s} {:s}".format(first_name, last_name))
