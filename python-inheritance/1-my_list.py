#!/usr/bin/python3
"""class that inherits the list"""


class MyList(list):

    """MyList inherits list"""
    def print_sorted(self):
        print(sorted(self))
