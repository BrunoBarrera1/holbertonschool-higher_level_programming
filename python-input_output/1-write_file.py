#!/usr/bin/python3
"""
this block contains a function
"""


def write_file(filename="", text=""):
    """this function will write the file"""
    text = "hello world"
    with open("example.txt,", "w") as file:
        file.write(text)
