#!/usr/bin/python3
"""
Module for appending a string to the end of a text file
and returning the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file and returns the number of characters.
    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.
    Returns:
        int: The number of characters added.
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        return file.write(text)
