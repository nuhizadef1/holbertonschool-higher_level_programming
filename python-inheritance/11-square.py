#!/usr/bin/python3
"""
Module that defines class Square inheriting from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square, inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initialize a new Square.

        Args:
            size (int): size of the square's sides.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size <= 0.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Return the area of the square.
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Return the square description in format: [Square] <width>/<height>
        """
        return ("[Square] {}/{}"
                .format(self._Rectangle__width, self._Rectangle__height))
