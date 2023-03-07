def insertionSort(customList):
    for i in range(1, len(customList)):
        key = customList[i]
        j = i - 1
        while j >= 0 and key < customList[j]:
            customList[j + 1] = customList[j]
            j -= 1
        customList[j + 1] = key
    print(customList)

clist= [3,5,1,5,37,2,5,2]
insertionSort(clist) # [1, 2, 2, 3, 5, 5, 5, 37]
