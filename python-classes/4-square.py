#!/usr/bin/python3
"""this module defines a square"""


class Square:
    """class that defines square"""

    def __init__(self, size=0):
        """initialize square with optional size
        args: size int
        raises: typerror if it isnt an int
        valueerror if is less than 0
        """
        self.__size = size

        @property
        def size(self):
            return self.__size
        """returns value"""

        @size.setter
        def size(self, value):
            self.__size = value
            """Set the size of the square with validation.
            Args:
            value (int): The new size to set.
            Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
            """
        if not isinstance(self.size, int):
            raise TypeError("size must be an integer")
        if self.size < 0:
            raise ValueError("size must be >= 0")

        self.__size = self.size

        def area(self):
            return self.__size ** 2
            """returns square area"""
