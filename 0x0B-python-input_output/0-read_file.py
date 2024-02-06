#!/usr/bin/python3
"""
Module for reading a text file and printing its content to stdout.
"""


def read_file(filename=""):
    """
    Reads a text file and prints its content to stdout.
    Args:
        filename (str): The name of the file to read.
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
