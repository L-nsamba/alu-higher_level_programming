#!/usr/bin/python3
def read_file(filename=""):
    """Read a text file (UTF-8) and print its contents to stdout.

    Args:
        filename (str): The path to the text file to be read. Defaults to empty string.
    """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end='')
