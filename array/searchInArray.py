arr1 = [1,2,3,4,5,6,7]

def searchInArray(array, value):
    for i in range(0, len(array)):
        if array[i] == value:
            return i;
    return "The element does not exist in this array"

print(searchInArray(arr1, 6))
