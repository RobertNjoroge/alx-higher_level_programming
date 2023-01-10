#!/usr/bin/python3
"""A function that represents a function appeing on UTF8 file"""


def append_write(filename="", text=""):
    """a function that appends the file.
    
    Args:
       filename: represents the name of file.
       text: represents the text to be appended.

    Returns:
         returns the number of characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
