#!/usr/bin/python3
"""
This module provides a function to print a person's full name.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints a person's full name in the format "My name is <first> <last>".

    Args:
        first_name: A string representing the first name
        last_name: A string representing the last name (optional, defaults
                  to empty string)

    Raises:
        TypeError: If first_name or last_name are not strings

    Returns:
        None (prints to stdout)
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
