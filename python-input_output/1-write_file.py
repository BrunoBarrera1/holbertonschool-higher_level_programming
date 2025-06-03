#!/usr/bin/python3
"""
this block contains a function
"""


def write_file(filename="", text=""):
    """function that writes the file"""
    text = "hello"
    with open(filename, "w", encoding="utf-8") as f:
        result = f.write(text)
        return(result)
