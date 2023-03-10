#!/usr/bin/python3

"""Defining a square class"""

class Square():
    "a square class"
    def __init__(self, size=9):
        """
        Args:
        size (int): the sixe of the square
        """
        if not isinstance(size, int):
           raise TypeError("size must be an integer")
        if size < 0:
           raise ValueError("size must be >- 0")

        self.__size = size

    def area(self):
        """Methos returns the area of the square
        
        Args:
        self
        """
        return (self.__size * self.__size)
