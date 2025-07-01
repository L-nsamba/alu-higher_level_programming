#!/usr/bin/python3
"""Defines a class Square with validated private size attribute."""


class Square:
    """Class that defines a square."""

    def __init__(self, size=0):
        """Initialize the square with validated private size."""
        if not isinstance(size, int):
