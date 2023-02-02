#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    mylist = list.copy(my_list)
    if (idx < 0 or idx > len(mylist)):
        return mylist
    for count in range(len(mylist)):
        if (count == idx):
            mylist[idx] = element
    return mylist
