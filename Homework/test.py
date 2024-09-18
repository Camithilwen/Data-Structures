sum = 0
for value in range(1,4):
    sum += value
#print(sum)

y = 0
z = 0
for x in range(5,7):
    if y > z:
        z, y = y, z
    y = y + x;
#print(x)
#print(y)
#print(z)

string1 = "hello"[:3] + "python"[0]
#print(string1)

newList = ["George", "John", "Thomas", "James"]
newList.pop()
newList.append("Andrew")
#print(newList)

myList = list()
fileObj = open("myfile.dat", "rb")
while True:    
   try:        
      item = pickle.load(fileObj)        
      myList.append(item)    
   except EOFError:      
      fileObj.close()        
      break
   print(myList)
   
   #function takes user's phone number
   def userPhone():