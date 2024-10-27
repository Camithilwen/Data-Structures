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

    def delete(self): #delete from the beginning of the list
        #time complexity O(1)
        #if the list is empty
        if self.head is None:
            return
        
        #otherwise, head -> next should revise to head->next
        self.head = self.head.next
        return

    def pop(self): #remove from the end of the list
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        probe = self.head
        while probe.next.next is not None:
            probe = probe.next
        probe.next = None
        return

    def __len__(self): #return the number of elements in the list
        if self.head is None:
            return 0
        count = 1 
        probe = self.head
        while probe.next is not None:
            count += 1
            probe = probe.next
        return count

    def indexOf(self, data):
        pass

    def copy(self):
        pass

    def __str__(self):
        if self.head is None:
            return "None"
        probe = self.head
        strBuf = ""
        while probe.next is not None:
            strBuf = strBuf + str(probe.data) + " -> "
            probe = probe.next
        strBuf = strBuf + "None"
        return strBuf
    
    def __add__(self, other): #append all nodes in the other list to current
        self_copy = self.copy()
        other_copy = other.copy()
        if other_copy.head is None:
            return self_copy
        if self_copy.head is None:
            return other_copy
        probe = self_copy.head
        while probe.next:
            probe = probe.next
        probe.next = other_copy.head
        return self_copy
        
    def __eq__(self, other):
        if len(self) != len(other):
            return False
        #Else iterate through two lists and for each node, compare its data
        #whenever you get unmatched data, return False.
        #If all data match and we reach the end of both lists, return True.
        probe1 = self.head
        probe2 = other.head
        
        while probe1:
            pass #to be finished
        return True
    
    def copy(self):
        #This is how to implement a true duplicate of a linked structure:
        if self.head is None:
            return None
        
        probe = self.head
        copyList = LinkedList()
        prevNode = Node(probe.data, None)

        copyList.head = prevNode 

        probe = probe.next

        while probe is not None:
            copy = Node(probe.data, None)
            prevNode.next = copy
            prevNode = copy
            probe = probe.next
        return copyList



            

#Sample usage to test
myLinkedList = LinkedList()
#print(myLinkedList)
myLinkedList.append(1)
myLinkedList.append(2)
myLinkedList.append(3)
myLinkedList.append(4)
#print(myLinkedList)
#print("Length: ", len(myLinkedList))
myLinkedList.insert(5)
#print(myLinkedList)
myLinkedList.delete()
#print(myLinkedList)
myLinkedList.pop()
#print(myLinkedList)
#print("Length: ", len(myLinkedList))


list2 = LinkedList()
for number in range(1, 12):
    list2.append(number)
print("List 2:", list2)
print("List 1 before copy-add:", myLinkedList)
copy1 = myLinkedList.copy()
copy2 = list2.copy()
list3 = copy1 + copy2 
print("List 1 after copy-add:", myLinkedList)
print("List 3:", list3)
#print("Length list 3:", len(list3))