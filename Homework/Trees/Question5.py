binary_tree_array = [0]

def left_child_index(index):
    return abs(2 * index + 1)

def right_child_index(index):
    return  abs(2 * index + 2)

def pre_order(index):
    if index >= len(binary_tree_array) or binary_tree_array[index] is None:
        return []
    return [binary_tree_array[index]] + pre_order(left_child_index(index)) + pre_order(right_child_index(index))

def in_order(index):
    if index >= len(binary_tree_array) or binary_tree_array[index] is None:
        return []
    return in_order(left_child_index(index)) + [binary_tree_array[index]] + in_order(right_child_index(index))

def post_order(index):
    if index >= len(binary_tree_array) or binary_tree_array[index] is None:
        return []
    return post_order(left_child_index(index)) + post_order(right_child_index(index)) + [binary_tree_array[index]]


def checkSize(index):
    while index >= len(binary_tree_array):
        binary_tree_array.extend([None] * len(binary_tree_array))

def insert(value, index):
    checkSize(index)
    if binary_tree_array[index] is None:
        binary_tree_array[index] = value
    elif value < binary_tree_array[index]:
        insert(value, left_child_index(index))
    else:
        insert(value, right_child_index(index))

def delete(value):
    index = binary_tree_array.index(value)
    def removeSubTree(index):
        binary_tree_array[index] = None
        leftChild = index * 2 + 1
        rightChild = index * 2 + 2
        if leftChild <= len(binary_tree_array):
            if binary_tree_array[leftChild]:
                removeSubTree(leftChild)
        if rightChild <= len(binary_tree_array):
            if binary_tree_array[rightChild]:
                removeSubTree(rightChild)
    removeSubTree(index)

    


if __name__ == "__main__":

    for i in range(-10, 0):
        insert(i, 0)
    for i in range(1, 11):
        insert(i, 0)
    
    print("Pre-order Traversal:", pre_order(0))
    print("In-order Traversal:", in_order(0))
    print("Post-order Traversal:", post_order(0))