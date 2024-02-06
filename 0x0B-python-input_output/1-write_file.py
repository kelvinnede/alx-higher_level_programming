#!/usr/bin/python3
"""
Module for writing a string to a text file
and returning the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file and returns the number of characters.
    Args:
        filename (str): The name of the file to write.
        text (str): The string to write to the file.
    Returns:
        int: The number of characters written.
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        return file.write(text)
