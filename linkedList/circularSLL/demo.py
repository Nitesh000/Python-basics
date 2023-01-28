#circular linked list
#pyright: reportOptionalMemberAccess=false

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        temp = self.head

        new_node.next = self.head

        if self.head is not None:
            while(temp.next != self.head):
                temp = temp.next
            temp.next = new_node
        else:
            new_node.next = new_node
        self.head = new_node

    def printList(self):
        if self.head is None:
            print("This is a empty list")
        else:
            temp = self.head
            while temp:
                print("  " + str(temp.data))
                temp = temp.next
                if temp == self.head:
                    break

cll = CircularLinkedList()
cll.push(1)
cll.push(2)
cll.push(3)
cll.push(4)
cll.push(5)
cll.printList()
