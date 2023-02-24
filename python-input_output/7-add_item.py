#!/usr/bin/python3
"""Write a script that adds all arguments to a Python list,
   and then save them to a file:
"""


import sys
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
"""
 Importing the functions load_from_json_file and save_to_json_file from the files
 8-load_from_json_file.py and 7-save_to_json_file.py.
"""

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
