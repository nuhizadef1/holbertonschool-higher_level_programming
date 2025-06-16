#!/usr/bin/python3
def islower(c):
    if len(c) != 1:
        return False  # Optional: handles invalid input length
    return ord('a') <= ord(c) <= ord('z')
