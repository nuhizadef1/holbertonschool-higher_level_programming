#!/usr/bin/python3
# Assume number is already assigned by some code you don't touch
import random
number = random.randint(-100, 100)  # This line is given and should not be changed
print(number, end=' ')  # Print the number followed by a space, no newline yet
if number > 0:
    print("is positive")
elif number == 0:
    print("is zero")
else:
    print("is negative")
