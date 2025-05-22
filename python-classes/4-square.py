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
        self.size = size

        def size(self):
            """retrieve size of square"""
            return self.__size

        def size(self, value):
            """set the size of square with validation
            args: value int: new size to set
            raises: typeerror if it is not an int
            valueerror: if size is less than 0
            """
        if size not isinstance(value, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

        def area(self):
            """return area of the square"""
            return self.__size ** 2
