#!/usr/bin/python3

"""Defining a function"""

def matrix_divided(matrix, div):
    """A function that divides all elements of a matrix"""
    matrix = []
    for elms in matrix:
        list(elms)
        if not isinstance(matrix[elms], (int, float)):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        elif isinstance(matrix[elms], (int, float)):
            matrix.append(elms)

    for sec in matrix:
         list(sec)
         if not isinstance(matrix[sec], (int, float)):
             raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
         elif isinstance(matrix[sec], (int, float)):
             matrix.append(sec)
       
