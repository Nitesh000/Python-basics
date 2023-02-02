# Queue with list and no size limit
#pyright: reportOptionalMemberAccess=false, reportOptionalIterable=false, reportOptionalSubscript=false,

class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        vlaues = [str(x) for x in self.items]
        return " ".join(vlaues)

    # isEmpty
    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    # enQueue
    def enQueue(self,value):
        self.items.append(value)
        return "The element is inserted at he end of the queue."

    # deQueue
    def deQueue(self):
        if self.isEmpty():
            return "There aren't any elements in the queue."
        else:
            self.items.pop(0)
            return "The element has been removed form the queue."

    # peek
    def peek(self):
        if self.isEmpty():
            return "There aren't any elements in the queue."
        else:
            return self.items[0]

    # delete
    def delete(self):
        self.items = None
            


customQ = Queue()
customQ.enQueue(1) # The element is inserted at he end of the queue.
customQ.enQueue(2) # The element is inserted at he end of the queue.
customQ.enQueue(3) # The element is inserted at he end of the queue.
print(customQ) # 1 2 3
customQ.deQueue() # The element has been removed form the queue.
print(customQ) # 2 3
customQ.peek() # 2
customQ.delete() # None
print(customQ) # None
