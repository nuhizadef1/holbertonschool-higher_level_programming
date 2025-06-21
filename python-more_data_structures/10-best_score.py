#!/usr/bin/python3
def best_score(a_dictionary):
    """
    Returns the key with the biggest integer value in the dictionary.

    Args:
        a_dictionary (dict): Dictionary with values as integers.

    Returns:
        str or None: Key with the highest value, or None if dictionary is empty or None.
    """
    if not a_dictionary:
        return None

    best_key = None
    best_value = None

    for key in a_dictionary:
        if best_value is None or a_dictionary[key] > best_value:
            best_value = a_dictionary[key]
            best_key = key

    return best_key
