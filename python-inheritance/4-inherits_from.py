#!/usr/bin/python3
"""Write a function that returns True if the object is an instance
of a class that inherited (directly or indirectly) from the
pecified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """
    It checks if the object is an instance of a class that inherited
    from the specified class

    :param obj: object
    :param a_class: a class object
    """
    if type(obj) is a_class:
        return False
    else:
        return isinstance(obj, a_class)
