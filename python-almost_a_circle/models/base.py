#!/usr/bin/python3
"""Defines the Base class."""
class Base:
    """Base class for all other classes in this project.

    This class manages the id attribute for all derived classes
    and helps avoid code duplication.

    Attributes:
        __nb_objects (int): Count of objects when no id is given.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance.

        Args:
            id (int, optional): The identity of the new instance. 
                               If None, increments __nb_objects and uses that as id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
