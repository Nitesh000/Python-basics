# queue with linked list
# pyright: reportGeneralTypeIssues=false

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        itr = self.head
        while itr:
            yield itr
            itr = itr.next

class Queue:
    def __init__(self):
        self.linkedList = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.linkedList]
        return ' '.join(values)

    # enqueue
    def enqueue(self, value):
        node = Node(value)
        if self.linkedList.head == None:
            self.linkedList.head = node
            self.linkedList.tail = node
        else:
            self.linkedList.tail.next = node
            self.linkedList.tail = node

    # isEmpty 
    def isEmpty(self):
        if self.linkedList.head is None:
            return True
        else:
            return False

    # deQueue
    def deQueue(self):
        if self.isEmpty():
            return "The Queue is empty"
        else:
            temp = self.linkedList.head
            if self.linkedList.head == self.linkedList.tail:
                self.linkedList.head = None
                self.linkedList.tail = None
            else:
                self.linkedList.head = self.linkedList.head.next
            return temp

    # peek
    def peek(self):
        if self.isEmpty():
            return "The Queue is empty"
        else:
            return self.linkedList.head

customQueue = Queue()
print(customQueue.isEmpty()) # True
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue) # 1 2 3
customQueue.deQueue()
print(customQueue) # 2 3
print(customQueue.peek()) # 2

