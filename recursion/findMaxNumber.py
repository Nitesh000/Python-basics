def findMaxNumber(sampleArray, n):
    if n == 1:
        return sampleArray[0]
    return max(sampleArray[n-1], findMaxNumber(sampleArray, n-1))

arr = [33,32,6,12,453,44,23,63]
print(findMaxNumber(arr,8))
