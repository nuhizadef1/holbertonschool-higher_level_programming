#!/usr/bin/python3
from calculator_1 import add, subtract, multiply, divide

def main():
    a = 10
    b = 5

    result1 = add(a, b)
    print("Add: %d" % result1)

    result2 = subtract(a, b)
    print("Subtract: %d" % result2)

    result3 = multiply(a, b)
    print("Multiply: %d" % result3)

    result4 = divide(a, b)
    print("Divide: %d" % result4)

if __name__ == "__main__":
    main()
