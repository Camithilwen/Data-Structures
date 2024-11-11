from BST_Complete import BinarySearchTree

import random

myTree = BinarySearchTree()

#Add 8 random numbers from 1 to 100 inclusive into the tree.
# for i in range(8):
#     number = random.randrange(1, 101) #101 is excluded.
#     myTree.insert(number)

data = [23, 45, 11, 8, 4, 67, 49]
for value in data:
    myTree.insert(value)

print("In order traversal:")
myTree.in_order_traversal(myTree.root) #Data is automatically sorted. So cool!
print("\nPre order traversal:")
myTree.pre_order_traversal(myTree.root)
print("\nPost order traversal:")
myTree.post_order_traversal(myTree.root)
print("\n\nMax value in the tree:")
print(myTree.find_max().value)
print("\nMin value in the tree:")
print(myTree.find_min().value)

print("\nTree one:")
print(myTree)

data2 = [5, 3, 7, 2, 4, 6, 8]
myTree2 = BinarySearchTree()
for value in data2:
    myTree2.insert(value)
print("\nTree two:")
print(myTree2)