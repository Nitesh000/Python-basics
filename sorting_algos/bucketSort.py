import math
from insertionSort import insertionSort as isort

def bucketSort(customList):
    numberOfBuckets = round(math.sqrt(len(customList)))
    maxValue = max(customList)
    arr = []

    for i in range(numberOfBuckets):
        arr.append([])
    for j in customList:
        index_b = math.ceil(j * numberOfBuckets / maxValue)
        arr[index_b - 1].append(j)

    for i in range(numberOfBuckets):
        arr[i] = isort(arr[i])

    k = 0
    for i in range(numberOfBuckets):
        for j in range(len(arr[i])):
            customList[k] = arr[i][j]
            k += 1
    return customList

clist= [5,3,2,7,8,4,1,6]
sortedClist = bucketSort(clist)
print(sortedClist) # [1, 2, 3, 4, 5, 6, 7, 8]
            

