#!/usr/bin/python3
"""
this block contains a function
"""


def write_file(filename="", text=""):
    """function that writes the file"""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
