def selectionSort(customList):
    for i in range(len(customList)):
        minIndex = i
        for j in range(i+1, len(customList)):
            if customList[minIndex] > customList[j]:
                minIndex = j
        customList[i], customList[minIndex] = customList[minIndex], customList[i]
    print(customList)

clist= [3,5,1,5,37,2,5,2]
selectionSort(clist) # [1, 2, 2, 3, 5, 5, 5, 37]
