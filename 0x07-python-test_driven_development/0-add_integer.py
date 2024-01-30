#!/usr/bin/python3
"""
This module provides a function to add two integers.

"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int or float): The first operand.
        b (int or float, default: 98): The second operand.

    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
