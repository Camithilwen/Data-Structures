#Python code to implement a stack using singly linked list.
#Next time we will implement a stack using Python list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Reference to the next node
#Operations for a stack:
# push(): insert a data into the top of the stack
# pop(): pop out the top element
# peek() or top(): return the top element's data. However, the 
# stack is intact.


class Stack:
    def __init__(self): #create an empty stack
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, data):  #push the data into the stack
        #Linked list is a FIFO data structure so 
        #for stack, we use its insert() method.
        new_node = Node(data)

        #Check if we have stack overflow, which means
        #we couldn't get more memory for the new element.
        if new_node is None:
            raise MemoryError("\nStack Overflow\n")
        
        #link the new node to the top of the stack
        new_node.next = self.head

        #update the top
        self.head = new_node

    def pop(self): #to remove the top element from the stack 
        #make sure the stack is not empty
        if self.head is None:
            raise IndexError("\nStack Underflow\n")
        else:
            #copy the top element to a temp variable
            temp = self.head

            #update the top
            self.head = self.head.next

            #return the variable
            return temp.data
    def peek(self):
        if self.head is None:
            print("\nStack is empty\n")
        else:
           return self.head.data
        
    def __str__(self):
        if self.head is None:
            return "None"
        else:
            current_node = self.head
            strBuf = " Top <- "
            while current_node:
                strBuf = strBuf + str(current_node.data) +" <- "
                current_node = current_node.next

            strBuf = strBuf + "Bottom of the stack"
            return strBuf
    
    def __len__(self):
        if self.head is None:
                return 0
        count = 1 
        probe = self.head
        while probe.next is not None:
            count += 1
            probe = probe.next
        return count 
    
    def size(self):
        return len(self)
    
    def __iter__(self):
       probe = self.head
       while probe:
           yield probe.data
           probe = probe.next 

#Test stack
#Create a Stack
if __name__ == "__main__":

    myStack = Stack()

    myStack.push(11)
    myStack.push(22)
    myStack.push(33)
    myStack.push(44)
    myStack.push(55)

    print(myStack)

    print("The top of the stack is ", myStack.peek())

    print("Popping out a data from the stack")
    myStack.pop()

    print("The top of the stack is ", myStack.peek())

    print("pushing 100 into the stack")
    myStack.push(100)
    print("The top of the stack is ", myStack.peek())

    print(myStack) #what if we want to print the stack in a format

    print("Stack size:", myStack.size())