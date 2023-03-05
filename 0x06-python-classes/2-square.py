#!/usr/bin/python3


""""Defining a square class"""


class Square:

    """A square class"""

    def __init__(self, size=0):
        """Initialises a square class
         Args:
         size (int): size of the new square

        """
        self.__size = size

        if size is int:
            try:
                pass
            except TypeError:
                print("size must be an integer")
        if size < 0:
            try:
                pass
            except ValueError:
                print('size must be >= 0')
