#!/usr/bin/python3
"""Module for saving Python objects to JSON files.

This module provides a function to serialize Python objects to JSON format
and save them to text files.
"""

import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON representation.

    Args:
        my_obj: The Python object to be serialized to JSON.
        filename (str): The name of the file to write to.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
