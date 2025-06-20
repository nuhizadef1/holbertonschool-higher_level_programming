#!/usr/bin/python3

print("".join(
    "{}".format(chr(c) if c % 2 == 1 else chr(c).upper())
    for c in range(ord('z'), ord('a') - 1, -1)
), end="")
