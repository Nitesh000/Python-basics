# usign the queue module for queue

import queue as q

customQueue = q.Queue(maxsize=3)
print(customQueue.qsize()) # 0
print(customQueue.empty()) # True
customQueue.put(1) # adding 1
customQueue.put(2) # adding 2
customQueue.put(3) # adding 3
print(customQueue.qsize()) # 3
print(customQueue.full()) # True
print(customQueue.get()) # 1
print(customQueue.get()) # 2
print(customQueue.get()) # 3
print(customQueue.qsize()) # 0

