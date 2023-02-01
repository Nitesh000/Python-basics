#Stack with linked list
#pyright: reportGeneralTypeIssues=false

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        itr = self.head
        while itr:
            yield itr
            itr = itr.next

class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return '\n'.join(values)

    #isEmpty
    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False

    #push
    def push(self, value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node

    #pop
    def pop(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            node = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return node

    #peek
    def peek(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            return self.LinkedList.head.value

    #delete
    def delete(self):
        self.LinkedList.head = None
        return "The stack has been successfully deleted"

customStack = Stack()
print(customStack.isEmpty()) #True
print(customStack.push(1)) #The element has been successfully inserted
print(customStack.push(2)) #The element has been successfully inserted
print(customStack.push(3)) #The element has been successfully inserted
print(customStack) # 3 2 1
print(customStack.isEmpty()) #False
print(customStack.pop()) # 3
print(customStack.peek()) # 2
print(customStack.delete()) # The stack has been successfully deleted 
print(customStack.isEmpty()) #True
