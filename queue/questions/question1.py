# Describe how you could use a singly python list to implement three stacks.

class MultiStack:
    def __init__(self, stackSize):
        self.numberStacks = 3
        self.custList = [0] * (stackSize * self.numberStacks)
        self.sizes = [0] * self.numberStacks
        self.stackSize = stackSize

    def isFull(self, stackNum):
        if self.sizes[stackNum] == self.stackSize:
            return True
        else:
            return False

    def isEmpty(self, stackNum):
        if self.sizes[stackNum] == 0:
            return True
        else:
            return False

    def indexOfTop(self, stackNum):
        offset = stackNum * self.stackSize
        return offset + self.sizes[stackNum] -1 

    def push(self, item, stackNum):
        if self.isFull(stackNum):
            return "The stack is full"
        else:
            self.sizes[stackNum] += 1
            self.custList[self.indexOfTop(stackNum)] = item

    def pop(self,stackNum):
        if self.isEmpty(stackNum):
            return "The stack is Empty"
        else:
            value = self.custList[self.indexOfTop(stackNum)]
            self.custList[self.indexOfTop(stackNum)] = 0
            self.sizes[stackNum] -= 1
            return value

    def peek(self, stackNum):
        if self.isEmpty(stackNum):
            return "The stack is empty"
        else:
            value = self.custList[self.indexOfTop(stackNum)]
            return value

customStack = MultiStack(5)
print(customStack.isFull(0)) # False
print(customStack.push(1,0)) # None
print(customStack.push(2,0)) # None
print(customStack.isEmpty(0)) # False
customStack.push(3,2) 
customStack.push(4,2)
print(customStack.peek(2)) # 4
print(customStack.pop(0)) # 2
