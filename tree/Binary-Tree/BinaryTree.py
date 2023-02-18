# Creation of Binary Tree: Using Linked List
# pyright: reportGeneralTypeIssues=false

from inOrderTra import inOrderTraversal
from preOrderTra import preOrderTraversal
from postOrderTra import postOrderTraversal

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


preOrderTraversal(newBT) #Drinks Hot Cold
inOrderTraversal(newBT) #Hot Drinks Cold
postOrderTraversal(newBT) #Hot Cold Drinks
