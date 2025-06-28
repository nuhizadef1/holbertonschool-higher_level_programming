#!/usr/bin/python3
"""
Module that defines class Square which inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square based on Rectangle.
    """

    def __init__(self, size):
        """
        Initialize a new Square.

        Args:
            size (int): The size of the square sides.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is <= 0.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
