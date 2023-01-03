#!/usr/bin/python3
"""Defines a Rectangle class"""


class Rectangle:
    """A new rectangle
       number of instances"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes a rectangle instance
        Args:
           width: width of rectangle.
           height: height of rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Returns an informal printable string representation
        of a rectangle instance, filled with #character."""
        if self.__height == 0 or self.__width == 0:
            return ''
        rec_str = ''
        for i in range(self.__height):
            for j in range(self.__width):
                rec_str += '#'
            rec_str += '\n'
        return rec_str[:-1]

    def __repr__(self):
        """Returns a string representation of Rectangle by using
        eval()"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Deletes a rectangle instance."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -=1

    @property
    def width(self):
        """Retrieves the width of a rectangle instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of a Rectangle instance."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of a Rectangle instance"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of a Rectangle instance"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of a Rectangle instanc"""
        if self.__height == 0 or self.__weight == 0:
            return 0
        return 2 *(self.__width + self.__height)
