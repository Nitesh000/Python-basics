# pyright: reportOptionalSubscript=false
# pyright: reportGeneralTypeIssues=false

class BinaryTree:
    def __init__(self, size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

    def insertNode(self, value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "The Binary Tree is full"
        self.customList[self.lastUsedIndex + 1] = value
        self.lastUsedIndex += 1
        return "The value has been successfully inserted"

    def searchNode(self, nodeValue):
        for i in range(len(self.customList)):
            if self.customList[i] == nodeValue:
                return "Success"
        return "Not found"

    def preOrderTraversal(self,index):
        if index > self.lastUsedIndex:
            return
        print(self.customList[index])
        self.preOrderTraversal(index * 2)
        self.preOrderTraversal(index * 2 + 1)

    def inOrderTraversal(self,index):
        if index > self.lastUsedIndex:
            return 
        self.inOrderTraversal(index * 2)
        print(self.customList[index])
        self.inOrderTraversal(index * 2 + 1)

    def postOrderTraversal(self,index):
        if index > self.lastUsedIndex:
            return
        self.postOrderTraversal(index * 2)
        self.postOrderTraversal(index * 2 + 1)
        print(self.customList[index])

    def levelOrderTraversal(self,index):
        for i in range(index, self.lastUsedIndex+1):
            print(self.customList[i])

    def deleteNdoe(self, value):
        if self.lastUsedIndex == 0:
            return "There is no element in the Binary Tree"
        for i in range(1, self.lastUsedIndex + 1):
            if self.customList[i] == value:
                self.customList[i] = self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex -= 1
                return "The node has been successfully deleted"
        return "Node not found"

    def deleteBT(self):
        self.customList = None
        return "The Binary Tree has been successfully deleted"

newBT = BinaryTree(8)
newBT.insertNode("Drinks")
newBT.insertNode("Hot") 
newBT.insertNode("Cold")
newBT.insertNode("Tea")
newBT.insertNode("Coffee")

newBT.preOrderTraversal(1) # Drinks Hot Tea Cold Coffee
newBT.inOrderTraversal(1) # Tea Hot Coffee Drinks Cold
newBT.postOrderTraversal(1) # Tea Coffee Hot Cold Drinks
newBT.levelOrderTraversal(1) # Drinks Hot Cold Tea Coffee
newBT.deleteNdoe("Tea") # The node has been successfully deleted
