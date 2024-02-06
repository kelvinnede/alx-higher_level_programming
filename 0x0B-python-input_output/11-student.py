#!/usr/bin/python3
"""
Module for defining a Student class
with serialization and deserialization methods.
"""


class Student:
    """
    Represents a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance
        with first name, last name, and age.
        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation
        of a Student instance with filter.
        Args:
            attrs (list): A list of strings
            specifying the attributes to include.
        Returns:
            dict: The dictionary representation
            of the student with filtered attributes.
        """
        if attrs is None:
            return self.__dict__
        return {
            attr: getattr(self, attr)
            for attr in attrs
            if hasattr(self, attr)
        }

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student
        instance with values from a dictionary.
        Args:
            json (dict): A dictionary representing
            the attributes of the student.
        """
        for key, value in json.items():
            setattr(self, key, value)
