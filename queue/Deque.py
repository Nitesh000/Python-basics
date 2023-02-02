# using the collection(deque) module for queue
from collections import deque

customQueue = deque(maxlen=3)
print(customQueue) # deque([])

customQueue.append(1)
customQueue.append(2)
customQueue.append(3)
print(customQueue) # deque([1, 2, 3], maxlen=3)
customQueue.append(4)
print(customQueue) # deque([2, 3, 4], maxlen=3) // it overwrites the first element
print(customQueue.popleft()) # 2
print(customQueue) # deque([3, 4], maxlen=3)
customQueue.clear()
print(customQueue) # deque([], maxlen=3)
