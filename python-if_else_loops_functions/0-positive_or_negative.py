#!/usr/bin/python3
import random
random.seed(0)
number = random.randint(-100, 100)
print(number, end=' ')
if number > 0:
    print("is positive")
elif number == 0:
    print("is zero")
else:
    print("is negative")
