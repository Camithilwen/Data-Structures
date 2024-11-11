from recursiveBST import BinarySearchTree

import random

myTree = BinarySearchTree()

for i in range(8):
    number = random.randrange(1, 101)
    myTree.insert(number)

print(myTree)