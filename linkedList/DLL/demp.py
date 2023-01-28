#Creation of doubly linked list
class Node:
    def __init__(self, data,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data,self.head)
        self.head = node

    def print_all(self):
        if self.head == None:
            print("The list is empty")
        else:
            temp = self.head
            lst = ""
            while temp:
                lst += str(temp.data) + "<-->"
                temp = temp.next
            print(lst)
                
dll = DoublyLinkedList()            
dll.insert_at_beginning(5)
dll.insert_at_beginning(4)
dll.insert_at_beginning(3)
dll.insert_at_beginning(2)
dll.insert_at_beginning(1)
dll.print_all()
