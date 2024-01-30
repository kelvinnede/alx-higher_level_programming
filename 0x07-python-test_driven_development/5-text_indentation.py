#!/usr/bin/python3
"""
This module provides a function
To print a text with 2 new lines after each of these characters: ., ? and :

"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = [".", "?", ":"]
    lines = []

    for char in text:
        lines.append(char)
        if char in separators:
            lines.append("\n\n")

    print("".join(lines), end="")
