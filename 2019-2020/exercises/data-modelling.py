
class BinaryTree:
    def __init__(self, root):
        if isinstance(root, Node):
            self.__root = root
            print("Binary tree created!")
        else:
            print("No root: ERROR")
    
    def getRoot(self):
        return self.__root
    
    def computeHeight(self, node):
        if node is None:
            return 0
        else:
            return 1 + max(
                self.computeHeight(node.getLeftChild()), 
                self.computeHeight(node.getRightChild()))
        
class Node:
    def __init__(self, value, leftChild=None, rightChild=None):
        self.__value = value 
        if isinstance(leftChild, Node):
            self.leftChild = leftChild
        else:
            self.leftChild = None
            #print("The object you provided as left child is not an instance of the class Node")
        if isinstance(rightChild, Node):
            self.rightChild = rightChild
        else:
            self.rightChild = None
            #print("The object you provided as right child is not an instance of the class Node")
        
    def getValue(self):
        return self.__value
    
    def removeValue(self):
        self.__value = None
    
    def getLeftChild(self):
        return self.leftChild
    
    def setLeftChild(self, leftChild):
        if isinstance(leftChild, Node):
            self.leftChild = leftChild
        else:
            self.leftChild = None
            
    def removeLeftChild(self):
        self.leftChild = None
        
    def isLeftChildAvailable(self):
        if self.leftChild is not None:
            return True
        else:
            return False
        
    def getRightChild(self):
        return self.rightChild
        
    def setRightChild(self, rightChild):
        if isinstance(rightChild, Node):
            self.rightChild = rightChild
        else:
            self.rightChild = None
            
    def removeRightChild(self):
        self.rightChild = None
        
    def isRightChildAvailable(self):
        if self.rightChild is not None:
            return True
        else:
            return False
        
#btree1 = BinaryTree(2)
#rightChild = Node(5)

root = Node(value=2, leftChild=Node(5))

btree2 = BinaryTree(root)
height = btree2.computeHeight(btree2.getRoot())
print(height)
#print(btree2.getRoot().getValue())

leftChild = Node(7)

#print("Left child before adding it : " + str(root.getLeftChild()))
#root.setLeftChild(leftChild)
#print("Left child after adding it : " + 
#      str(root.getLeftChild().getValue()))

