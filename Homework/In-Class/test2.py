newList = list(range(9,0,-3))
print(newList)
newObject =  tuple("Hello")
print(newObject)
yourObject = "Hi"
myObject = tuple(yourObject)
print (myObject)

myList = [2, 3 ,5 ,7 ,11]
yourList = list(myList)
r = yourList is myList
print(r)
print(yourList)

mySet = {2, 3, 5, 6, 11}
yourSet = {5, 7, 2, 11, 3}
r = yourSet == mySet
print (r)