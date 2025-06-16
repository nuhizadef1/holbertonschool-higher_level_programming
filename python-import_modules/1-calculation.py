#!/usr/bin/python3
from calculator_1 import add, subtract, multiply, divide

def main():
    a = 10
    b = 5
    result1 = add(a, b)
    print("Add: {}".format(result1))
    result2 = subtract(a, b)
    print("Subtract: {}".format(result2))
    result3 = multiply(a, b)
    print("Multiply: {}".format(result3))
    result4 = divide(a, b)
    print("Divide: {}".format(result4))

if __name__ == "__main__":
    main()
