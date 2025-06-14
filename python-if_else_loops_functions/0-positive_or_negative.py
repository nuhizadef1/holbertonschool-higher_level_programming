#!/bin/usr/python3
# Assume number is already assigned by some code you don't touch
print(f"{number} ", end="")

if number > 0:
    print("is positive")
elif number == 0:
    print("is zero")
else:
    print("is negative")
