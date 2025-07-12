#!/usr/bin/python3
def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): The name of the file to read.
    """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end='')
