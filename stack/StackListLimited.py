#limited list stack
#pyright: reportGeneralTypeIssues=false
#pyright: reportOptionalSubscript=false, reportOptionalMemberAccess=false

class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.stack = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    #isEmpty
    def isEmpty(self):
        if self.stack == []:
            return True
        else:
            return False

    #isFull
    def isFull(self):
        if len(self.stack) == self.maxSize:
            return True
        else:
            return False

    #push
    def push(self, value):
        if self.isFull():
            return "The stack is full"
        else:
            self.stack.append(value)
            return "The element has been successfully inserted"

    #pop
    def pop(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            return self.stack.pop()

    #peek
    def peek(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            return self.stack[-1]

    #delete
    def delete(self):
        self.stack = None
        return "The stack has been successfully deleted"

customStack = Stack(5)
print(customStack.isEmpty()) #True
print(customStack.push(1)) #The element has been successfully inserted
print(customStack.push(2)) #The element has been successfully inserted
print(customStack.push(3)) #The element has been successfully inserted
print(customStack.isEmpty()) #False
print(customStack.isFull()) #False
print(customStack.push(4)) #The element has been successfully inserted
print(customStack.push(5)) #The element has been successfully inserted
print(customStack.push(6)) #The stack is full
print(customStack.isFull()) #True
print(customStack.pop()) # 5
print(customStack.peek()) # 4
print(customStack.delete()) #The stack has been successfully deleted
