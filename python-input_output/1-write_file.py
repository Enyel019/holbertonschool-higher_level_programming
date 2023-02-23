#!/usr/bin/python3
"""Write a function that writes a string to a text file (UTF8)
   and returns the number of characters written:
"""


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF8) and return the number
    of characters written.

    :param filename: the name of the file to write to
    :param text: the text to write to the file
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
        return len(text)
