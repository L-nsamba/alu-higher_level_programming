#!/usr/bin/python3
"""Module for loading objects from JSON files.

This module provides a function to deserialize JSON data from files
into Python objects.
"""

import json


def load_from_json_file(filename):
    """Create an object from a JSON file.

    Args:
        filename (str): The path to the JSON file to read.

    Returns:
        object: The Python object represented by the JSON data in the file.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
