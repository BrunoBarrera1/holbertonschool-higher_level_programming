#!/usr/bin/python3
"""Defines class rectangle."""


class Rectangle:
    """Represents rectangle."""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """returns long."""
        return self.__width

    @width.setter
    def width(self, value):
        """Establishes long."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """returns tall."""
        return self.__height

    @height.setter
    def height(self, value):
        """establishes tall."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
