#!/usr/bin/python3
"""
Module for converting a JSON string to an object (Python data structure).
"""


def from_json_string(my_str):
    """
    Returns an object represented by a JSON string.
    Args:
        my_str (str): The JSON string to convert to an object.
    Returns:
        obj: The object represented by the JSON string.
    """
    import json
    return json.loads(my_str)
