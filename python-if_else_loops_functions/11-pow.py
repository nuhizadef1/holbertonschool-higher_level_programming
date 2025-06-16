#!/usr/bin/python3
def pow(a, b):
    # Handle the case of b == 0
    if b == 0:
        return 1

    # Handle negative powers
    if b < 0:
        a = 1 / a
        b = -b

    result = 1
    for _ in range(b):
        result *= a

    return result
