from BinarySearchTree import BinarySearchTree
import random

myTree = BinarySearchTree()
#add 8 random numbers between 1 and 100 (inclusive) into the tree
for i in range(8):
    number = random.randrange(1, 101) #101 is excluded by this range function.
    myTree.insert(number)
print(myTree)
