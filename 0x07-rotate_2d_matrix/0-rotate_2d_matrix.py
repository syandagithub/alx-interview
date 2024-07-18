#!/usr/bin/python3
"""
Rotate 2D Matrix.
"""

def rotate_2d_matrix(matrix):
    """Rotates an n x n 2D matrix in place by 90 degrees clockwise.
    Args:
         matrix (list[[list]]): a matrix
    """
    n = len(matrix)
    for i in range(int(n / 2)):
        y = (n - i - 1)
        for j in range(i, y):
            x = (n - 1 - j)
            tmp = matrix[i][j]
            matrix[i][j] = matrix[x][i]
            matrix[x][i] = matrix[y][x]
            matrix[y][x] = matrix[j][y]
            matrix[j][y] = tmp
