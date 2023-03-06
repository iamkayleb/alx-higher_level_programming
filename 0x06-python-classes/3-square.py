#!/usr/bin/python3

"""Define a square"""


class Square:
    """a square class"""

    def __init__(self, size=0):
        """Initialises a square
          Args:
          self (int): size of square

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        "returns area of the square"
        return (self.__size * self.__size)
