#!/usr/bin/python3
"""
Module for converting an instance of a class
to a dictionary for JSON serialization.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    for JSON serialization of an object.
        Args:
        obj: An instance of a class.
    Returns:
        dict: The dictionary representation of the object.
    """
    attributes = obj.__dict__
    for key in list(attributes.keys()):
        if key.startswith("__") and not key.endswith("__"):
            attributes[key.lstrip("_")] = attributes.pop(key)
    return attributes
