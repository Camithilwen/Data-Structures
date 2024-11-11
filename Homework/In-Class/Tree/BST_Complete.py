class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    '''Properties of BST:
        - All values to the left side of the tree are smaller
        - All values to the right are larger.'''
    def __init__(self):
        self.root = None

    # 1. Insert a node
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    # 2. Search for a node
    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None or node.value == value: #No match or data found
            return node
        if value < node.value: #Recurse left for search target
            return self._search_recursive(node.left, value)
        else: #Recurse right for search target
            return self._search_recursive(node.right, value)

    # 3. Delete a node
    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if node is None:
            return node

        # Traverse the tree to find the node
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            # Node with one or no children
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node with two children: get the inorder successor
            temp = self.find_min(node.right)
            node.value = temp.value
            node.right = self._delete_recursive(node.right, temp.value)

        return node

    # 4. Find minimum node
    def find_min(self, node=None):
        if node is None:
            current = self.root
        else:
            current = node

        while current and current.left:
            current = current.left
        return current

    # 5. Find maximum node
    def find_max(self, node=None):
        if node is None:
            current = self.root
        else:
            current = node

        while current and current.right:
            current = current.right
        return current

    # 6. In-order traversal
    def in_order_traversal(self, node):
        if node:
            self.in_order_traversal(node.left)
            print(node.value, end=" ")
            self.in_order_traversal(node.right)

    # 7. Pre-order traversal
    def pre_order_traversal(self, node):
        if node:
            print(node.value, end=" ")
            self.pre_order_traversal(node.left)
            self.pre_order_traversal(node.right)

    # 8. Post-order traversal
    def post_order_traversal(self, node):
        if node:
            self.post_order_traversal(node.left)
            self.post_order_traversal(node.right)
            print(node.value, end=" ")
    
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

    # Example Usage
    bst = BinarySearchTree()

    # Insert nodes
    numbers = [10, 5, 15, 3, 7, 13, 18]
    for number in numbers:
        bst.insert(number)

    # Search for a value
    print("Search for 7:", bst.search(7) is not None )  # Output: True
    print("Search for 100:", bst.search(100) is not None)  # Output: False

    # Delete a node
    bst.delete(10)

    # Traversals
    print("In-order Traversal:")
    bst.in_order_traversal(bst.root)  # Should print the values in ascending order

    print("\nPre-order Traversal:")
    bst.pre_order_traversal(bst.root)  # Should print root first

    print("\nPost-order Traversal:")
    bst.post_order_traversal(bst.root)  # Should print root last

    # Find min and max
    print("\nMinimum value:", bst.find_min().value)  # Should be the smallest element
    print("Maximum value:", bst.find_max().value)  # Should be the largest element
