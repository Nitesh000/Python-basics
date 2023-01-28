class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    #insert at the start of a singly linked list
    def insert_at_start(self, data):
        node = Node(data, self.head)
        if self.head == None:
            self.tail = node
        self.head = node

    #insert at the end of the singly linked list
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = new_node
        
    #Print all elements
    def print_all(self):
        if self.head is None:
            print("This is a empty linked list")
        itr = self.head
        lst = ""
        while itr:
            lst += str(itr.data) + "-->"
            itr = itr.next
        print(lst)

    #Search for value in the linked list
    def search_for(self, data):
        if self.head == None:
            return "The list is not present"
        else:
            itr = self.head
            pos = 0
            while itr is not None:
                if itr.data == data:
                    print(f"{data}: is in position of {pos}.")
                    return
                pos += 1
                itr = itr.next
            print("The {data} is not present in the linked list.")
            return

    #Delete node of singly linked list
    def delete_node(self, location):
        if self.head is None:
            print("The singly linked list does nto exist.")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next


  
slist = SLinkedList();
slist.insert_at_start(4);
slist.insert_at_start(2);
slist.insert_at_end(10);
slist.print_all()
slist.search_for(10)
