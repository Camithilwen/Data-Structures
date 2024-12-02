from listStack import Stack

data = [34, 4, 31, 89, 78, 23]

dataStack = Stack()
#push all data items into the stack.
for number in data:
    dataStack.push(number)

#Now we can use the temp stack sort it
tempStack = Stack()
while not dataStack.isEmpty():
    number = dataStack.peek() #read the top data item
    dataStack.pop() #remove the top element from the data stack.

    #push the data into the temp stack and make sure it remains in order
    while not tempStack.isEmpty() and tempStack.peek() < number:
        dataStack.push(tempStack.peek()) #move the item to data stack
        tempStack.pop()
    
    tempStack.push(number)

print(tempStack)
