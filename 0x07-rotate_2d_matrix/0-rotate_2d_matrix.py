#!/usr/bin/python3
"""Rotate 2D Matrix.
"""

def rotate_2d_matrix(matrix):
    """Rotates an n x n 2D matrix in place by 90 degrees clockwise.
    Args:
         matrix (list[[list]]): a matrix
    """
    n = len(matrix)
    if n != len(matrix[0]):
        raise ValueError("Matrix must be square")

    # Rotate the matrix in place
    for layer in range(n / 2):
        first = layer
        last = n - layer - 1
        for i in range(first, last):
            offset = i - first
            top = matrix[first][i]
            matrix[first][i] = matrix[last - offset][first]
            matrix[last - offset][first] = matrix[last][last - offset]
            matrix[last][last - offset] = matrix[i][last]
            matrix[i][last] = top
