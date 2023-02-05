#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    ls = []
    for count in range(0, list_length):
        r = 0
        try:
            r = my_list_1[count] / my_list_2[count]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            ls.append(r)
    return ls
