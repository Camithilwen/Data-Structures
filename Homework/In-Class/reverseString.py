from listStack import Stack

def reverseString(inputString):
    stack = Stack()

    for char in inputString:
        stack.push(char)
    reverseString = "" 
    while not stack.isEmpty():
        reverseString += stack.peek()
        stack.pop()
    
    return reverseString

inputStr = "Shepherd University"
print("The reverse string of Shepherd is", reverseString(inputStr))

