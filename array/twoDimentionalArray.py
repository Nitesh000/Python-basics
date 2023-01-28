import numpy as np

twoDArray = np.array([[1,2,3,4,5],[5,4,3,2,1]])

print(twoDArray)

# create and print another 2D array
# anotherTwoDArray = np.array([[1,2,3,4,5],[5,4,3,2,1],[1,2,3,4,5],[5,4,3,2,1]])

# print(anotherTwoDArray)

# def accessElements(array, rowIndex, colIndex):
#     if rowIndex >= len(array) and colIndex >= len(array[0]):
#         print("Invalid row or column index")
#     else:
#         print(array[rowIndex][colIndex])
#
# accessElements(twoDArray, 2, 2)

# traversal of two dimensional array

# def traverseTwoDArray(array):
#     for i in range(len(array)):
#         for j in range(len(array[0])):
#             print(array[i][j], end=" ")
#         print()
#    
# traverseTwoDArray(twoDArray)

# searching for element in two dimensional array

# def searchTwoDArray(array, value):
#     for i in range(len(array)):
#         for j in range(len(array[0])):
#             if array[i][j] == value:
#                 return 'The value is found at index: ' + str(i) + ',' + str(j)
#     return 'The value is not found'
#
# print(searchTwoDArray(twoDArray, 5))

# deleteing in two dimensional array
newTwoDArray = np.delete(twoDArray, 1, 0)
print(newTwoDArray)
