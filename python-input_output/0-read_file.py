#!/usr/bin/python3
"""Write a function that reads a text file (UTF8) and prints it to stdout:
"""


def read_file(filename=""):
    """
    This function reads a file and prints it to the standard output.

    :param filename: the name of the file to read
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
