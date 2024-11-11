class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    '''All data to the left is smaller than the value of the node.
       All data to the right is larger than the value of the node.'''
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root is None
    
    def insert(self, value):

        if self.root is None:
            self.root = Node(value) 
            return
        else:
            self.recursiveInsert(value, self.root)

    def recursiveInsert(self, value, node):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self.recursiveInsert(value, node.left)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self.recursiveInsert(value, node.right)



    def __str__(self):
        '''helper method for printing the tree
           print result: (20) -- one node
           3 nodes: ((1) 2 (3))
           4 nodes: ((1) 2 (3 (4)))'''
        return self.recursivePrint(self.root)
    
    def recursivePrint(self, node):
        if node is None:
            return ""
        
        return f"({self.recursivePrint(node.left)}{node.value}{self.recursivePrint(node.right)})"
    
if __name__ == "__main__":
    myTree = BinarySearchTree()
    print(myTree)

    myTree.insert(2)
    print(myTree)

    myTree.insert(1)
    myTree.insert(3)
    print(myTree)
    myTree.insert(4)
    print(myTree)