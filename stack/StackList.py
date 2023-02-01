# stack wihout size limit
# pyright: reportOptionalMemberAccess=false
# pyright: reportOptionalSubscript=false
# pyright: reportOptionalIterable=false

class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    # isEmpty
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    # push
    def push(self, value):
        self.list.append(value)
        return "The element has been successfully inserted"

    # pop
    def pop(self):
        if self.isEmpty():
            return "There is no element in the Stack"
        self.list.pop()
        return "The element has been successfully deleted"

    # peek
    def peek(self):
        if self.isEmpty():
            return "There is no element in the Stack"
        return self.list[-1]

    # delete
    def delete(self):
        self.list = None
        return "The stack has been successfully deleted"

customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack.isEmpty())
customStack.pop()
print(f"Peek: {customStack.peek()}")
print(customStack)
