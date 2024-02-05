#!/usr/bin/python3

def is_same_class(obj, a_class):
    """
    Check if obj is an instance of a_class.

    Args:
    - obj: object to check
    - a_class: class to check against

    Returns:
    - True if obj is an instance of a_class, False otherwise
    """
    return type(obj) == a_class
