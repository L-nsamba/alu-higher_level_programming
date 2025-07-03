#!/usr/bin/python3
"""
This module defines a Rectangle class that keeps track of the
number of instances and allows calculation of area and perimeter.
It also provides string representations using '#' characters.
"""


class Rectangle:
    """Represents a rectangle with width and height.

    Tracks the number of instances created and deleted.
    """

    number_of_instances = 0  # Corrected variable name (was number_of_instances)

    def __init__(self, width=0, height=0):
        """Initialize the rectangle with optional width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width, ensuring it's a non-negative integer."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height, ensuring it's a non-negative integer."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return the informal string representation using '#'."""
        if self.__width == 0 or self.__height == 0:
            return ""
        lines = ["#" * self.__width for _ in range(self.__height)]
        return "\n".join(lines)

    def __repr__(self):
        """Return the official string representation."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print message when instance is deleted and decrement counter."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
