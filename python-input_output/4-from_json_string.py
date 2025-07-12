#!/usr/bin/python3
"""
Module that provides JSON string parsing functionality.
"""
import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string.

    Args:
        my_str (str): The JSON string to parse.

    Returns:
        object: The Python object represented by the JSON string.
    """
    return json.loads(my_str)
