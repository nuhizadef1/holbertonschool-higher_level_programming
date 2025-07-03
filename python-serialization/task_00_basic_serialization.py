#!/usr/bin/env python3
import json

def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary to a JSON file.

    Parameters:
    - data: A Python dictionary to be serialized.
    - filename: The name of the file where the serialized data will be saved.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Data has been serialized and saved to {filename}.")
    except Exception as e:
        print(f"An error occurred while saving to file: {e}")

def load_and_deserialize(filename):
    """
    Loads and deserializes JSON data from a file into a Python dictionary.

    Parameters:
    - filename: The name of the file to load the data from.

    Returns:
    - A Python dictionary containing the deserialized data.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except Exception as e:
        print(f"An error occurred while loading the file: {e}")
        return None
