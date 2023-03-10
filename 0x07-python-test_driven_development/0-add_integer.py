#!/usr/bin/python3
"""
This is the addition module

This module supplies one function that adds two integers together

"""


def add_integer(a, b=98):
    """
    Function adds two integers together.

    Args:
    a (int); first integer
    b (int): second integer

    FLoats are converted to integers
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
