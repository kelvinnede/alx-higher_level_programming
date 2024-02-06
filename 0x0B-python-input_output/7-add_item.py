#!/usr/bin/python3
"""
Script for adding arguments to a Python list and saving them to a file.
"""

import sys
from os.path import exists
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

# File name to save the list
filename = "add_item.json"

# Initialize an empty list or load existing list from file
if exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

# Add arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list to file
save_to_json_file(my_list, filename)
