#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """
    Returns a new dictionary with all values multiplied by 2.

    Args:
        a_dictionary (dict): The original dictionary with integer values.

    Returns:
        dict: A new dictionary with values multiplied by 2.
    """
    new_dict = {}
    for key in a_dictionary:
        new_dict[key] = a_dictionary[key] * 2
    return new_dict
