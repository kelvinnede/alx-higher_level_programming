#!/usr/bin/python3
"""
This module contains a class Square that defines a square.
"""


class Square:
    """
    This class represents a square.
    """

    def __init__(self, size):
        """
        Initializes a new instance of the Square class.

        Args:
            size: The size of the square.

        Note:
            The size attribute is a private instance attribute.
        """
        self.__size = size
