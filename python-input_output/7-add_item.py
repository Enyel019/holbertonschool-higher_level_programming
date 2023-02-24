#!/usr/bin/python3
"""Write a script that adds all arguments to a Python list,
   and then save them to a file:
"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# This is a try/except block. If the file add_item.json exists,
#         it will load the list from the file. If the file does not exist,
#         it will create an empty list.
try:
    list = load_from_json_file('add_item.json')
except FileNotFoundError:
    list = []

# Adding the arguments to the list.
list.extend(sys.argv[1:])

# Saving the list to a file named add_item.json.
save_to_json_file(list, 'add_item.json')
