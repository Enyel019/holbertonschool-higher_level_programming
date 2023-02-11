#!/usr/bin/python3
"""Write a function that prints a text with 2 new lines after each of
   these characters: ., ? and :
"""


def text_indentation(text):
    """
    This function takes a string as input and prints it with two new lines after each of these
    characters: ., ? and :

    :param text: a string
    """
    msg_1 = "text must be a string"
    if not isinstance(text, str):
        raise TypeError(msg_1)
    text = text.strip()
    l = len(text)
    id = 0
    while id in range(l):
        if text[id] == '?' or text[id] == ':' or text[id] == '.':
            if text[id] == '?':
                print('?')
            if text[id] == ':':
                print(':')
            if text[id] == '.':
                print('.')
            print()
            id += 1
            for idd in range(id, l):
                if text[idd] == ' ':
                    idd += 1
                    id = idd
                if text[idd] != ' ':
                    break
        print(text[id], end='')
        id += 1
