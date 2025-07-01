#!/usr/bin/python3
"""Module that defines a Square class with a size property and area method."""


class Square:
    """Class that defines a square."""

    def __init__(self, size=0):
        """Initialize the square with a validated private size."""
        self.size = size  # This uses the setter for validation

    @property
    def size(self):
        """Getter: Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter: Set and validate the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size * self.__size
