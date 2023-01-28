# How to create a Tuple?

myTuple = (1,6,2,7,19)
myTuple1 = (1,4,2,5,3)

print(myTuple + myTuple1) # prints (1, 6, 2, 7, 19, 1, 4, 2, 5, 3)
print(myTuple * 2) # prints (1, 6, 2, 7, 19, 1, 6, 2, 7, 19)
print(7 in myTuple) # prints True

print(myTuple.count(7)) # prints 1
print(myTuple.index(7)) # prints 3
print(len(myTuple)) # prints 5
print(max(myTuple)) # prints 19
print(min(myTuple)) # prints 1

print(tuple([1,2,3,4])) # prints (1, 2, 3, 4)
