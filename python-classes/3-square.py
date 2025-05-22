#!/usr/bin/python3

"""module defines square now it is commented passplez"""
class Square:
    """a class that defines a square"""


    def __init__(self, size=0):
        """initialize a square  with an optional size.
        args:
        size (int): the size of the square
        raises:
        typeerror: if size is not an integer
        valueerror: if sie is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """return the area of the square"""
        return self.__size ** 2
