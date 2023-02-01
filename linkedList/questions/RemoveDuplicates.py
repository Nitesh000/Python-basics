# Question:  Remove Duplicates: Write a code to remove duplicated from an unsorted linked list
from LinkedList import LinkedList

def removeDups(ll):
    if ll.head is None:
        return 
    else:
        itr = ll.head
        visited = set([itr.value])
        while itr.next:
            if itr.next.value in visited:
                itr.next = itr.next.next
            else:
                visited.add(itr.next.value)
                itr = itr.next
        return ll

# Here is a way to doing it without using the temperal buffer. 
def removeDups1(ll):
    if ll.head is None:
        return

    itr = ll.head
    while itr:
        runner = itr
        while runner.next:
            if runner.next.value == itr.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        itr = itr.next
    return ll.head


customLL = LinkedList()
customLL.generate(10, 0, 99)
print(customLL)
# removeDups(customLL)
removeDups1(customLL)
print(customLL)
