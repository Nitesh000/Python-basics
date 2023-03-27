def linearSearch(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return i
    return -1

returnValue = linearSearch([1, 2, 3, 4, 5], 3)
print(returnValue) # 2
