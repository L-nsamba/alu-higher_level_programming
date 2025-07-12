#!/usr/bin/python3
"""
Module that provides file reading functionality.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints it to stdout.

    Args:
        filename (str): The name of the file to read. Defaults to empty string.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content, end='')
