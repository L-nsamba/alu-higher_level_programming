#!/usr/bin/python3
"""Defines a base geometry class with an unimplemented area method."""


class BaseGeometry:
    """Base class for geometry objects."""

    def area(self):
        """Raise an exception indicating the area method is not implemented."""
        raise Exception("area() is not implemented")
