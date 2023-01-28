# Create a linked list
# pyright: reportGeneralTypeIssues=false
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_the_beginning(self, data):
        node = Node(data)
        if self.head == None:
           self.head = node
        else:
            node.next = self.head
            self.head = node

    def print_all(self):
        if self.head == None:
            print("The linked list is empty")
        else:
            lst = ""
            itr = self.head
            while itr:
                lst += str(itr.data) + "-->"
                itr = itr.next
            print(lst)

llst = LinkedList()
llst.insert_at_the_beginning(1)
llst.insert_at_the_beginning(2)
llst.insert_at_the_beginning(3)
llst.insert_at_the_beginning(4)
llst.print_all()
