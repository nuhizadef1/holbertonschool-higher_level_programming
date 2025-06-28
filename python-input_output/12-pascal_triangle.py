#!/usr/bin/python3
# -*- coding: utf-8 -*-

def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        prev_row = triangle[i - 1]

        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])

        row.append(1)
        triangle.append(row)

    return triangle


def main():
    n = int(input("Pascal üçbucağının sətrin sayı: "))
    triangle = pascal_triangle(n)
    for row in triangle:
        print(row)


if __name__ == "__main__":
    main()

