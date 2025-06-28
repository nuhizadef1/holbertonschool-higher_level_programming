#!/usr/bin/python3
"""
Defines a Student class with serialization and deserialization methods.
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Instantiates a Student object.

        Args:
            first_name (str): Student's first name
            last_name (str): Student's last name
            age (int): Student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.

        Args:
            attrs (list, optional): List of attribute names to retrieve.
                                    If None, returns all attributes.

        Returns:
            dict: Dictionary representation of the Student instance.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            result = {}
            for attr in attrs:
                if hasattr(self, attr):
                    result[attr] = getattr(self, attr)
            return result
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with values from json.

        Args:
            json (dict): Dictionary with attribute names as keys and attribute values.
        """
        for key, value in json.items():
            setattr(self, key, value)
