# Rotate Matrix = Given an matrix by an NxN matrix write a method to rotate the image by 90 degrees.
import numpy as np

myArray = np.array([[1,2,3],[4,5,6],[7,8,9]])

def rotateMatrix(matrix):
    n = len(matrix)
    for i in range(n//2):
        first = i
        last = n - i - 1
        for j in range(first,last):
            # save top element
            top = matrix[i][j]
            # move top element to top
            matrix[i][j] = matrix[-j-1][i]

