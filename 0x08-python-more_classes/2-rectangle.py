#!/usr/bin/python3
"""Defining a class Rectangle"""

class Rectangle:
    """Represent new Rectangle"""
    def __init__(self, width=0, height=0):
        """ Initialize new rectangle

        Args:
           width (int): The width of new rectangle
           height (int): The height of new rectangle
        """
        self.width = width
        self.height = height

    @propety
    def width(self):
        """Get/set the width"""
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """Get/set the height"""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        """Return area"""
        return ((self.__width) * (self.__height))

    def perimeter(self):
        """Return the perimeter"""
        return ((self.__width + self.__width) + (self.__height + self.__height))

