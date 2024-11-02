class Stack:
    def __init__(self):
        self.items =[] 

    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)  #we view the end of the list as top of stack
    
    def pop(self):  #remove the top element, return nothing
        if not self.is_empty():
            self.items.pop()
        else:
            raise IndexError("Stack underflow")
    
    def peek(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            return self.items[-1]
        
    def size(self):
        return len(self.items)

    def __str__(self):
        if len(self.items) > 0:
            strBuf = f"\nTop\n|\nV\n"
            for i in self.items:
                strBuf = strBuf + f"{i}\n|\nV\n"
            strBuf = strBuf + "Bottom"
            return strBuf
        else:
            return "Stack is empty"

if __name__ == "__main__":  
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(5)
    stack.push(8)

    print("The number of elements in the stack:",stack.size())
    print("The value of top element:", stack.peek())
    
    stack.pop()

    print("The number of elements in the stack:",stack.size())
    print("The value of top element:", stack.peek())
    
    print("Stack:", stack)