#!/usr/bin/python3
"""
module: 2-square
Defines class square with a private size attribute
"""


class Square:
    """class defining square"""

    def __init__(self, size=0):
        """initialize square
        args:
        size int: size of square
        raises:
        typeerroR: if size is not an integer
        valueerror: if size is less than 0
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
