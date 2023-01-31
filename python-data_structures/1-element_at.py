#!/usr/bin/python3
def element_at(my_list, idx):
    if (idx < 0 or idx > len(my_list)):
        return None
    for count in range(len(my_list)):
        if (count == idx):
            return my_list[idx]
