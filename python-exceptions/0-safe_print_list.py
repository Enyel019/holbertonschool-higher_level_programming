#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        for count in range(0, x):
            print(my_list[count], end="")
            i += 1
        print()
        return(i)
    except IndexError:
        print()
        return(i)
