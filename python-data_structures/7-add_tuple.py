#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    l1 = list(tuple_a)
    l2 = list(tuple_b)
    l1.append(0)
    l1.append(0)
    l2.append(0)
    l2.append(0)
    l3 = [l1[0] + l2[0], l1[1] + l2[1]]
    l3 = l3[:3]
    return(tuple(l3))
