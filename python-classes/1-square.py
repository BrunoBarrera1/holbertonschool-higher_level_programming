#!/usr/bin/python3
"""
Module: 1-square
Defines class square with a private sie attribute.
"""

class Square:
    """
    Class Square that defines a square via a private instance attribute: size

    private instance attribute:
    __size (int): the size of the square, set on instantiation without validation.

    Why private?
    the size of a square is funcamental for operations like area computation. by making it private,
    the class builder can control andvalidate type and value in future tasks.
    """
    def __init__(self, size):
        """
        initialize a new Square instance sithout validation.

        Args:
        size (int): the size of the square
        """
        self.__size = size
