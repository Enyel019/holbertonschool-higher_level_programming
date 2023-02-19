#!/usr/bin/python3
class MyList(list):
    """It's a list that can be sorted by the second element of
    each tuple in the list
    """
    def print_sorted(self):
        """It prints the elements of the list in sorted order.
        """
        print(sorted(self))
