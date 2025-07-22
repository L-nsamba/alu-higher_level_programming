#!/usr/bin/python3
"""
This module provides a function to format text with special indentation.

The main function text_indentation prints text with 2 new lines after
specific punctuation marks: period (.), question mark (?), and colon (:).
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after '.', '?' and ':' characters.

    Args:
        text (str): The input text to be formatted and printed.

    Raises:
        TypeError: If text is not a string.

    The function removes leading and trailing spaces from each printed line
    and adds exactly 2 new lines after '.', '?', and ':' characters.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n")
            i += 1
            # Skip any whitespace that comes after the punctuation
            while i < len(text) and text[i] in ' \t':
                i += 1
        else:
            i += 1
