#!/usr/bin/python3
"""This module defines a custom list class with a sorted print method."""


class MyList(list):
    """MyList is a subclass of list with an additional print_sorted method."""

    def print_sorted(self):
        """Print the list in ascending sorted order without modifying the list itself."""
        print(sorted(self))
