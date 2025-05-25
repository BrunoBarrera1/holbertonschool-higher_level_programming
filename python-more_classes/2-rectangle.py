#!/usr/bin/python3

"""
module that defines a rectangle
"""


class Rectangle:
    """class that defines the rectangle"""
    def __init__(self, width=0, height=0):
        """init a new rectangle instance"""
        self.width = width
        self.height = height

        @property
        def width(self):
            """retrieve long of rectangle"""
            return self.__width

        @width.setter(self, value):
            """set the width"""
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

            @property
            def height(self):
                """retrieve tall"""
                return self.__height

            @height.setter
            def height(self, value):
                """im not commenting, i just lost someone"""
                if not isinstance(value, int):
                    raise TypeError("height must be an integer")
                if value < 0:
                    raise ValueError("height must be >= 0")
                self.__height = value

                def area(self):
                    """
                    a
                    """
                    return self.width * self.__height

                def perimeter(self):
                    """a"""
                    if self.__width == or self.__height == 0:
                        return 0
                    return 2 * (self.__width + self.__height)
