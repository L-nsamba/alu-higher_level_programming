#!/usr/bin/python3
"""Module that defines a Square class with size and position."""


class Square:
    """Class that defines a square with size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize square with optional size and position."""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Getter: Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter: Set and validate the position of the square."""
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not isinstance(value[0], int) or
            not isinstance(value[1], int) or
            value[0] < 0 or
            value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with '#' using size and position."""
        if self.__size == 0:
            print()
            return

        # Print newlines based on position[1]
        for _ in range(self.__position[1]):
            print()

        # Print each row of the square with spaces based on position[0]
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
