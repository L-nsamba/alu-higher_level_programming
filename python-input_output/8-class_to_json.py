#!/usr/bin/python3
def class_to_json(obj):
    """Returns the dictionary description
       for JSON serialization of an object.

    Args:
        obj: An instance of a class with serializable attributes.

    Returns:
        dict: A dictionary containing all
        serializable attributes of the object.
    """
    return obj.__dict__
