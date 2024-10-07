class Node: #a basic unit for a linked structure.
    def __init__(self, data, next):
        self.data = data
        self.next = next

#Let's build a linked list using the node class
class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, data): #add data to the end of the list.
        new_node = Node(data, None) #create new node
        #add the new node to the list
        if self.head is None: #if the list is empty, set the head as the new node
            self.head = new_node
            return
        #otherwise, place the new node at the end of the list
        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next

        last_node.next = new_node
        return
    #add to the beginning on the list
    def insert(self, data):
        new_node = Node(data, None)

        #if the current list is empty
        if self.head is None:
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head = new_node
        return
    
    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end="--->")
            current_node = current_node.next
        print("None")

#Sample usage to test
myLinkedList = LinkedList()
myLinkedList.append(1)
myLinkedList.append(2)
myLinkedList.append(3)
myLinkedList.append(4)
myLinkedList.print_list()
myLinkedList.insert(5)
myLinkedList.print_list()