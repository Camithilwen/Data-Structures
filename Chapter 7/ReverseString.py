from stackWithLinkedList import Stack

def reverse_string(input_string):
    stack = Stack()

    for char in input_string:
        stack.push(char)
    
    reverse_string = ''
    while not stack.is_empty():
        reverse_string += stack.peek()
        stack.pop()

    return reverse_string

input_str = "Shepherd University" 
print("The reverse string is " + reverse_string(input_str))