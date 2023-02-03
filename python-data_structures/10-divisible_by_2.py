#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    mlist = list.copy(my_list)
    for count in range(len(my_list)):
        if (my_list[count] % 2 == 0):
            mlist[count] = 1
        elif (my_list[count] % 2 != 0):
            mlist[count] = 0
    return(mlist)
