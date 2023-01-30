#circular doubly linked list 
#pyright: reportOptionalMemberAccess=false
class Node:
    def __init__(self, data=None,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class CDLL:
    def __init__(self,head=None,tail=None):
        self.head = head
        self.tail = tail

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    def print_all(self):
        if self.head is None:
            print("The CDLL is empty.")
        else:
            itr = self.head
            lst = ""
            while itr:
                lst += str(itr.data) + "<-->"
                itr = itr.next
                if itr == self.tail.next:
                    break
            print(lst)

    def reverse(self):
        if self.tail is None:
            print("The CDLL is empty.")
        else:
            itr = self.tail
            lst = ""
            while itr:
                lst += str(itr.data) + "<-->"
                itr = itr.prev
                if itr == self.head.prev:
                    break
            print(lst)

    def createCDLL(self, nodeValue):
        node = Node(nodeValue)
        self.head = node
        self.tail = node
        node.next = node
        node.prev = node
        print("The CDLL is created successfully.")

    def insert(self, data, location):
        if self.head is None:
            print("The CDLL is empty.")
        else:
            node = Node(data)
            if location == 0:
                node.next = self.head
                node.prev = self.tail
                self.head.prev = node
                self.head = node
                self.tail.next = node
            elif location == -1:
                node.next = self.head
                node.prev = self.tail
                self.tail.next = node
                self.tail = node
                self.head.prev = node
            else:
                itr = self.head
                index = 0
                while index < location - 1:
                    itr = itr.next
                    index += 1
                node.next = itr.next
                node.prev = itr
                itr.next = node
                node.next.prev = node

    def search(self, data):
        if self.head is None:
            print("The CDLL is empty.")
        else:
            itr = self.head
            index = 0
            while itr:
                if itr.data == data:
                    print(f"The {data} is found at index of {index}")
                    break
                itr = itr.next
                index += 1
                if itr == self.tail.next:
                    print("The data is not found.")
                    break

    def delete(self, location):
        if self.head is None:
            print("The CDLL is empty.")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                itr = self.head
                index = 0
                while index < location - 1:
                    itr = itr.next
                    index += 1
                itr.next = itr.next.next
                itr.next.prev = itr

    def delelte_all(self):
        if self.head is None:
            print("The CDLL is empty.")
        else:
            self.tail.next = None
            itr = self.head
            while itr:
                itr.prev = None
                itr = itr.next
            self.head = None
            self.tail = None
            print("The CDLL is deleted successfully.")
        
cdll = CDLL()
cdll.createCDLL(1) # The CDLL is created successfully.
cdll.print_all() # 1
cdll.insert(2,0)
cdll.insert(3,0)
cdll.insert(4,0)
cdll.print_all() # 4<-->3<-->2<-->1
print([node.data for node in cdll]) # [4, 3, 2, 1]
cdll.insert(5,-1)
cdll.print_all() # 4<-->3<-->2<-->1<-->5
cdll.reverse() # 5<-->1<-->2<-->3<-->4
cdll.search(5) # The 5 is found at index of 4
cdll.delete(2) 
cdll.print_all() # 4<-->3<-->1<-->5
cdll.delelte_all() # The CDLL is deleted successfully.
cdll.print_all() # The CDLL is empty.
