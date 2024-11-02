class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0
    
    def push(self, item):
        '''Because append adds items to the end of a list, we view the end of the list as the top of the stack.'''
        self.items.append(item)
    
    def pop(self):
        '''Removes the top element of the stack (final element of the list) and returns no data.'''
        if not self.isEmpty():
            self.items.pop()
        else:
            raise ValueError("Stack underflow")
    
    def peek(self):
        '''Returns the value of the top item without altering the list.'''
        if self.isEmpty():
            print("Stack is empty.")
        else:
            return self.items[-1]
    
    def size(self):
        '''Return the size of the stack as equivalent to the length of the internal list.'''
        return len(self.items)

if __name__ == "__main__":
    stack = Stack()

    for i in range(0, 5):
        stack.push(i)
    
    print("The number of elements in the stack is:", stack.size())
    print("The value of the top element is", stack.peek())

    stack.pop()

    print("The number of elements in the stack is:", stack.size())
    print("The value of the top element is", stack.peek())


'''Let's apply a list stack by using the stack to reverse a string.
   We can push characters in the string into the stack and then pop the characters back out.'''