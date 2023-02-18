# pyright: reportGeneralTypeIssues=false
# pyright: reportOptionalMemberAccess=false
import QueueLinkedList as queue
def searchBT(rootNode, nodeValue):
    if not rootNode:
        return "The binary tree does not exist"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.deQueue()
            if root.value.data == nodeValue:
                return "Scuccess"
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
                 
