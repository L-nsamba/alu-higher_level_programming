#!/usr/bin/python3
"""
Module that provides class to JSON dictionary conversion functionality.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    for JSON serialization of an object.

    Args:
        obj: An instance of a Class with serializable attributes.

    Returns:
        dict: Dictionary representation of the object's attributes.
    """
    return obj.__dict__
