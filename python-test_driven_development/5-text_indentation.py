#!/usr/bin/python3
"""
This module provides a function to print text with indentation after
certain punctuation marks.
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after '.', '?' and ':' characters.

    Args:
        text: A string to be formatted and printed

    Raises:
        TypeError: If text is not a string

    Returns:
        None (prints to stdout)

    Note:
        No spaces at the beginning or end of each printed line.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n")
            i += 1
            # Skip any spaces after the punctuation
            while i < len(text) and text[i] == ' ':
                i += 1
        else:
            i += 1
