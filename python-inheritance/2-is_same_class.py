#!/usr/bin/python3
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
