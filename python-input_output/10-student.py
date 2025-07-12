#!/usr/bin/python3
"""Defines a Student class with JSON serialization capabilities."""


class Student:
    """Represents a student with basic information and JSON serialization."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student instance.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of the Student instance.

        Args:
            attrs (list, optional): List of attribute names to include.
                                   If None, includes all attributes.

        Returns:
            dict: Dictionary containing the requested attributes.
        """
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}
        return self.__dict__
