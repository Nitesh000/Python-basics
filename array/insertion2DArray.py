# insertion on 2D array

import numpy as np

twoDArray = np.array([[1,2,3,4,5],[5,4,3,2,1],[1,2,3,4,5],[5,4,3,2,1]])
print(twoDArray)

newTwoDArray = np.insert(twoDArray, 2, [[9,8,7,6]], axis=1)
print(newTwoDArray)

