from array import array
# 1. Create an array and traverse. 
print("Step 1")
arr = array("i",[1,2,3,4,5,6,7,8])
for i in arr:
    print(i)


# 2. Access individual elements through indexes
print("Step 2")
print(arr[3])

# 3. Append any value to the array using append() method
print("Step 3")
arr.append(9)
print(arr)

# 4. Insert value in an array using insert() method
print("Step 4")
arr.insert(0,0)
print(arr)
# 5. Extend python array using extend() method
print("Step 5")
arr.extend([11,12])
print(arr)
# 6. Add items from list into array using fromlist() method


# 7. Remove any array element using remove() method
print("Step 7")
arr.remove(0)
print(arr)
# 8. Remove last array element using pop() method
print("Step 8")
arr.pop()
print(arr)
# 9. Fetch any element through its index using index() method
print("Step 9")
arr.index(3)
print(arr)
# 10. Reverse a python array using reverse() method
print("Step 10")
arr.reverse()
print(arr)

# 11. Get array buffer information through buffer_info() method
print("Step 11")
print(arr.buffer_info())


# 12. Check for number of occurrences of an element using count() method
print("Step 12")
print(arr.count(2))
# 13. Convert array to string using toString() method
print("Step 13")
strTemp = map(str, arr)
print(strTemp)


# 14. Convert array to a python list with same elements using tolist() method
print("Step 14")
print(arr.tolist())
# 15. Append a string to char array using fromstring() method
# print("Step 15")


# 16. Slice Elements from an array
print("Step 16")
print(arr[2:4])
