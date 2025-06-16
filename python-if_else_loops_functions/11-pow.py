#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        return 1
    if b < 0:
        a = 1 / a
        b = -b
    result = 1
    for _ in range(b):
        result *= a
    return result

# Example of printing the output formatted to 2 decimal places:
print(f"{pow(0.1, 2):.2f}")
