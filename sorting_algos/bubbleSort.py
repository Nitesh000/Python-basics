def bubbleSort(customList):
    for i in range(len(customList)-1):
        for j in range(len(customList)-i-1):
            if customList[j] > customList[j+1]:
                customList[j], customList[j + 1] = customList[j + 1], customList[j]
    print(customList)

clist= [3,5,1,5,37,2,5,2]
bubbleSort(clist) # [1, 2, 2, 3, 5, 5, 5, 37]
