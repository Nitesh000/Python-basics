#pyright: reportOptionalMemberAccess=false
from random import randint
class Node:
    def __init__(self, value=None, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def __str__(self):  #for printing out the node
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):  # for able to print the nodes in the LinkedList
        itr = self.head
        while itr:
            yield itr
            itr = itr.next

    def __str__(self):
        values = [str(x.value) for x in self]
        return ' -> '.join(values)

    def __len__(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        return count

    def add(self, value):
        if self.head is None:
            self.head = Node(value, None, None)
            self.tail = self.head
        else:
            self.tail.next = Node(value, None, self.tail)
            self.tail = self.tail.next
        return self.tail

    def generate(self, n, min_value, max_value):
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(min_value, max_value))
        return self

# Just checking the code.
# customLL = LinkedList()
# customLL.generate(10, 0, 99)
# print(customLL) # 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 // some random numbers
# print(len(customLL)) # 10
