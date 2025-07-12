#!/usr/bin/python3
"""
Module that provides file appending functionality.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF-8) and
    returns the number of characters added.

    Args:
        filename (str): The name of the file to append to.
        Defaults to empty string.
        text (str): The text to append to the file.
        Defaults to empty string.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
