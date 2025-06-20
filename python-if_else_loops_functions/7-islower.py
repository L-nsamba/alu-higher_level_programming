#!/usr/bin/python3
def islower(c):
    """
    Check if a character is lowercase.

    Args:
        c: A single character

    Returns:
        True if c is a lowercase letter, False otherwise
    """
    # Get ASCII value of the character
    ascii_val = ord(c)

    # Lowercase letters have ASCII values from 97 ('a') to 122 ('z')
    return 97 <= ascii_val <= 122
