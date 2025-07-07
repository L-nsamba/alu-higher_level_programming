#!/usr/bin/python3
"""
Module that defines a MyList class that inherits from list
"""


class MyList(list):
    """
    MyList class that inherits from list

    Public methods:
        print_sorted(self): prints the list in ascending sorted order
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order
        Does not modify the original list
        """
        print(sorted(self))
