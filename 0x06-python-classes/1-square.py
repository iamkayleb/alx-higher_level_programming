#!/usr/bin/python3

""""Defines a new square"""


class Square:
    " a square class"

    def __init__(self, size):
        """Initialises a new square.

        Args:
            size (int): The size of the new square
        """
        self.__size = size
