#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    try:
        for count in range(0, x):
            try:
                if float(my_list[count]):
                    print("{:d}".format(my_list[count]), end="")
                    i += 1
            except ValueError:
                continue
        print()
        return(i)
    except TypeError:
        print()
        return(i)
