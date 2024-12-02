def inorder_traversal(root):
    recursive_traversal(root)

def recursive_traversal(node):
    if node is None:
        return
    
    recursive_traversal(node.left)
    process_data(node.data)
    recursive_traversal(node.right)