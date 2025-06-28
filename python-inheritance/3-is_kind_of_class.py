#!/usr/bin/python3
"""Function to check if an object is an instance of a class or its subclass.
"""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or its subclass, else False."""
    return isinstance(obj, a_class)
