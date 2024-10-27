#Python code to implement a stack using isngly linked list.
#Next time we will implement a stack using Python list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None #reference to the next node.

class Stack:
#Operations for a stack:
# push(): insert a data into the top of the stack.
# pop(): pop out the top element and return its data.
# peek() or top(): return the top element's data without altering the stack.
    def __init__(self): #create an empty stack.
        self.head = None

    def push(self, data): #push data into the stack.
        #Linked list is a FIFO data structure so for stack we use the insert() method.
        newNode = Node(data)

        #Check for stack overflow (where additional memory for the new element could not be found).
        if newNode == None:
            print("\nStack Overflow\n")

        #link the new node to the top of the stack
        newNode.next = self.head

        #update the top
        self.head = newNode

    def pop(self): #remove the top element of the stack and return the data
        #make sure the stack is not empty
        if self is None:
            print("\nStack Underflow\n")
        else:
            #copy the top element to a temporary variable.
            temp = self.head
            #update the top
            self.head = self.head.next
            #return memory space to OS manually (before garbage collection)
            del temp

    def peek(self):
        #check for empty stack
        if self is None:
            print("\nStack is empty\n")
        else:
            return self.head.data
    
    def __str__(self):
        if self.head is None:
            return None
        
        cursor = self.head
        strBuf = f"Top\n|\nV\n"
        while cursor.next:
            strBuf = f"{strBuf + str(cursor.data)}\n|\nV\n"
            cursor = cursor.next
        strBuf = strBuf + "Bottom"
        return strBuf


#Test the stack
#Create a stack
myStack = Stack()
for i in range(0, 6):
    myStack.push(i*11)
    
print("Top of stack:", myStack.peek())
print("Pop top!")
myStack.pop()
print("Top of stack:", myStack.peek())
print("Push 100!")
myStack.push(100)
print("Top of stack:", myStack.peek())
print(myStack)
