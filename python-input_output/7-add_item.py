#!/usr/bin/python3
"""Write a script that adds all arguments to a Python list,
   and then save them to a file:
"""

import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


# Trying to load the file add_item.json and if it does not exist,
# it will create it.
try:
    list = load_from_json_file('add_item.json')
# If the file does not exist, it will create it.
except FileNotFoundError:
    list = []


# Adding the arguments to the list.
list.extend(sys.argv[1:])


# Saving the list into the file add_item.json.
save_to_json_file(list, 'add_item.json')
