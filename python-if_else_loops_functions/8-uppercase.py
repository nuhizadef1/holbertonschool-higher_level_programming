#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        # Check if char is lowercase (ASCII 97 to 122)
        if ord(char) >= 97 and ord(char) <= 122:
            # Convert to uppercase by subtracting 32
            result += chr(ord(char) - 32)
        else:
            result += char
    print("{}".format(result))
