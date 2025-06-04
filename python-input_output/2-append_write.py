#!/usr/bin/python3

"""f"""


def append_write(filename="", text=""):
    """appends"""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
