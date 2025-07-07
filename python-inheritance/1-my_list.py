#!/usr/bin/python3
"""Defines a class MyList that inherits from list."""

class MyList(list):
    """Custom list class that inherits from built-in list."""

    def print_sorted(self):
        """Print the list in ascending sorted order (without modifying the original list)."""
        print(sorted(self))
