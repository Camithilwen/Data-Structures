from listStack import Stack

data = [20, 30, 40, 50, 60]

dataStack = Stack()

#Push all data into the stack
for number in data:
    dataStack.push(number)

##print(dataStack)
while not dataStack.isEmpty():
    print(dataStack.peek())
    dataStack.pop()