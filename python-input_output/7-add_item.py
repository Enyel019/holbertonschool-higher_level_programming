#!/usr/bin/python3
"""Write a script that adds all arguments to a Python list,
   and then save them to a file:
"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# Cargar la lista existente o crear una nueva si no existe el archivo
try:
    list = load_from_json_file('add_item.json')
except FileNotFoundError:
    list = []

# Agregar los argumentos a la lista
list.extend(sys.argv[1:])

# Guardar la lista en un archivo JSON
save_to_json_file(list, 'add_item.json')
