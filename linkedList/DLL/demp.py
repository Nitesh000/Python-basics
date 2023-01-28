#Creation of doubly linked list
#pyright: reportOptionalMemberAccess=false
class Node:
    def __init__(self, data,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    #Creation of doubly linked list
    def CreateDLL(self, data):
        node = Node(data)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node

    # Insertion method in custom position
    def insertNode(self, nodeValue, location):
        if self.head is None:
            print("The list is empty")
        else:
            newNode = Node(nodeValue)
            if location == 0:
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            elif location == -1:
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            else:
                itr = self.head
                count = 0
                while count < location - 1:
                    itr = itr.next
                    count += 1
                newNode.next = itr.next
                newNode.prev = itr
                itr.next = newNode
                newNode.next.prev = newNode
                    
    #Reverse traversal of doubly linked list
    def reverseTraversal(self):
        if self.head is Node:
            print("There isn't any elements on this DDL")
        else:
            itr = self.tail
            lst = ""
            while itr:
                lst += str(itr.data) + "<-->"
                itr = itr.prev
            print(lst)

    #Search of node in DLL
    def searchNode(self, nodeValue):
        if self.head is None:
            print("There aren't any elements in the DDL")
        else:
            itr = self.head
            pos = 0
            while itr:
                if itr.data == nodeValue:
                    return f"{nodeValue} is in the position of {pos}" 
                itr = itr.next
                pos += 1
            return f"{nodeValue} is not in this DLL"

    #deleting a node from DLL
    def deleteNode(self, location):
        if self.head is None:
            print("There aren't any elements to delete")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                itr = self.head
                count = 0
                while count < location -1:
                    itr = itr.next
                    count += 1
                itr.next = itr.next.next
                itr.next.prev = itr
            print("The node has been deleted")

    #deletion of entire DLl
    def deleteDLL(self):
        if self.head is None:
            print("There aren't any elements")
        else:
            itr = self.head
            while itr:
                itr.prev = None
                itr = itr.next
            self.head = None
            self.tail = None
            print("The whole DLL is deleted.")
        

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
dll.CreateDLL(5)
dll.insertNode(6,0)
dll.insertNode(7,0)
dll.insertNode(8,0)
dll.insertNode(9,0)
dll.print_all() # 9<-->8<-->7<-->6<-->5<-->
dll.reverseTraversal() # 5<-->6<-->7<-->8<-->9<-->
print(dll.searchNode(8)) # 8 is in the position of 1
dll.deleteNode(2)
dll.print_all() # 9<-->8<-->6<-->5<--> // 7 has been deleted
dll.deleteDLL()# The whole DLL is deleted.
dll.print_all() # The list is empty
