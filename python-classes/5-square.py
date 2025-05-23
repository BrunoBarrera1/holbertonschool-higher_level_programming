#!/usr/bin/python3
"""defines a square"""


class Square:
    """represents square"""

    def __init__(self, size=0):
        """initializes square"""
        self.size = size

        @property
        def size(self):
            """returns size of square"""
            return self.__size

        @size.setter
        def size(self, value):
            """establishes value of sq"""
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            if value < 0:
                raise ValueError("size must be >=0")
            self.__size = value

            def area(self):
                """returns area of square"""
                return self.__size ** 2

            def my_print(self):
                """prints # in the end"""
                if self.__size == 0:
                    print()
                else:
                    for _ in range(self.__size):
                        print("#" * self.__size)
