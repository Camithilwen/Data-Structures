"""
File: node.py

Node classes for one-way linked structures.
"""

class Node(object):

    def __init__(self, data, next = None):
        """Instantiates a Node with default next of None"""
        self.data = data
        self.next = next

#Just an empty link
node1 = None

#A node containing data and an empty link
node2 = Node("A", None)

#A nod containing data and a link to node2
node3 = Node("B", node2)

node4 = Node("C", node3)

#Now we have a singly linked list with three nodes.


#Building a linked list
head = None
size = 6
for count in range(1, size):
    head = Node(count, head)

#The above code will establish a linked list as follows:
#Iteration 1: count = 1, the linked list has one element: 1 --> None
#Iteration 2: count = 2, 2 nodes: 2 ---> 1
#Iteration 3: count = 3, 3 nodes, 3 --> 2 --> 1
# ...
#5: 5 --> 4 --> 3 --> 2 --> 1

