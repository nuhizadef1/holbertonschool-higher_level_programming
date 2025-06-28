#!/usr/bin/python3
"""
Function that returns the JSON representation of an object (string).
"""
import json


def to_json_string(my_obj):
    """
    Converts a Python object to a JSON string.

    Args:
        my_obj: Python object to convert.

    Returns:
        str: JSON representation of the object.
    """
    return json.dumps(my_obj)
