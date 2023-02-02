# Multiprocessing queue is a queue that can be shared between processes.

from multiprocessing import Queue

customQueue = Queue(maxsize=3)
customQueue.put(1) # adding 1
customQueue.put(2) # adding 2
customQueue.put(3) # adding 3
print(customQueue.full()) # True
print(customQueue.get()) # 1
