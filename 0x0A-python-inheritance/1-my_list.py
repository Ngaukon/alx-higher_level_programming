#!/usr/bin/python3


class MyList(list):
    """Class that inherits from list.

    Args:
        list (list): list to sort in ascending order.
    """
    def print_sorted(self):
        """Prints a list in ascending order.
        """
        list_ = self[:]
        list_.sort()
        print(list_)
