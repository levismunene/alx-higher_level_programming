#!/usr/bin/python3


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle"""
    def __init__(self, width, height):
        """Initializing"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates area"""
        return self.__width * self.__height

    def __str__(self):
        """Return info"""
        return "[Rectangle] " + str(self.__width) + '/' + str(self.__height)
