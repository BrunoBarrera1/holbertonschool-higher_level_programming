#!/usr/bin/python3
"""
this module defines a function that prints a file
"""


def read_file(filename=""):
    """function that does so"""
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
