class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Reference to the next node

# LinkedList class manages the nodes and operations of the linked list
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize an empty linked list
    
    def __str__(self):
        return "None"

    def append(self, data): #append to the end. O(n)
        new_node = Node(data)

        #if the linked list is empty
        if not self.head:
            self.head = new_node
            return
        
        #otherwise, we traverse to the end of the list (not the None node)
        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

    def insert(self, data): #insert to the beginning. O(1)
        new_node = Node(data)

        if not self.head: #if the current list is empty
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head = new_node
        return
    
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

    def delete(self): #delete from the beginning of the list
        #Time complexity: O(1)
        #if the list is empty
        if self.head is None:
            return
          
        #Otherwise, head should revise to head->next
        self.head = self.head.next
        return

    def pop(self): #remove from the end of the list
        #if the list is empty. Time complexity: average O(n)
        if self.head is None:
            return
        
        if self.head.next is None:  #if only one node in the list
            self.head = None
            return
        
        current = self.head     #Now the list with at least two data nodes
                                # current.next.next will not cause trouble
        while current.next.next is not None:
            current = current.next

        current.next = None
        return


    def length(self): #return the number of elements in the list
        #if the list is empty
        if self.head is None:
            return 0
        
        count = 1
        current = self.head
        while current.next is not None:
            count += 1
            current = current.next

        return count

# Example usage:
llist = LinkedList()

llist.append(1)
llist.append(2)
llist.append(3)
llist.print_list()
print("Length=", llist.length())

print(str(llist))
