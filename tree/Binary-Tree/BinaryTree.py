# Creation of Binary Tree: Using Linked List
# pyright: reportGeneralTypeIssues=false, reportOptionalMemberAccess=false

from inOrderTra import inOrderTraversal
from preOrderTra import preOrderTraversal
from postOrderTra import postOrderTraversal
from levelOrderTra import levelOrderTraversal
from SearchBT import searchBT
import QueueLinkedList as queue

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

newBT = TreeNode("Drinks") #Create a tree
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")
newBT.leftChild = leftChild
newBT.rightChild = rightChild
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
leftChild.leftChild = tea
leftChild.rightChild = coffee
rightChild = TreeNode("Cold")


preOrderTraversal(newBT) #Drinks Hot Tea Coffee Cold
inOrderTraversal(newBT) #Tea Hot Coffee Drinks Cold
postOrderTraversal(newBT) #Tea Coffee Hot Cold Drinks
levelOrderTraversal(newBT) #Drinks Hot Cold Tea Coffee
searchBT(newBT, "Tea") #The binary tree does not exist
searchBT(newBT, "Hot") #Success

def insertNodeBT(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.deQueue()
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            else:
                root.value.leftChild = newNode
                return "Successful Operation"

            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
            else:
                root.value.rightChild = newNode
                return "Successful Operation"

newNode = TreeNode("Cola")
print(insertNodeBT(newBT, newNode)) #Successful Operation
levelOrderTraversal(newBT) #Drinks Hot Cold Tea Coffee Cola

# pyright: reportUnboundVariable=false
def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.deQueue()
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
        deepestNode = root.value
        return deepestNode

def deleteDeepestNode(rootNode, dNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.deQueue()
            if root.value is dNode:
                root.vlaue = None
                return
            if root.value.rightChild:
                if root.value.rightChild is dNode:
                    root.value.rightChild = None
                    return
                else:
                    customQueue.enqueue(root.value.rightChild)
            if root.value.leftChild:
                if root.value.leftChild is dNode:
                    root.value.leftChild = None
                    return
                else:
                    customQueue.enqueue(root.value.leftChild)
def deleteNodeBT(rootNode, node):
    if not rootNode:
        return "The binary tree does not exist"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.deQueue()
            if root.value.data == node:
                dNode = getDeepestNode(rootNode)
                root.value.data = dNode.data
                deleteDeepestNode(rootNode, dNode)
                return "The node has been successfully deleted"
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
        return "failed to delete"

deleteNodeBT(newBT, "Tea")
levelOrderTraversal(newBT) #Drinks Hot Cold Coffee Cola

def deleteBT(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The binary tree has been successfully deleted"

deleteBT(newBT)
print("new BT")
levelOrderTraversal( newBT) #None None None None None
