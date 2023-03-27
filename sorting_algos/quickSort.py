def partition(customList, low, high):
    i = low - 1
    pivot = customList[high]
    for j in range(low, high):
        if customList[j] <= pivot:
            i += 1
            customList[i], customList[j] = customList[j], customList[i]
    customList[i+1], customList[high] = customList[high], customList[i+1]
    return (i + 1)

def quickSort(customList, low, high):
    if low < high:
        pi = partition(customList, low, high)
        quickSort(customList, low, pi - 1)
        quickSort(customList, pi + 1, high)


clist = [10, 7, 8, 9, 1, 5, 2, 3, 4, 6]
quickSort(clist, 0, len(clist) - 1)
print(clist) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
