myList = [24, 2, 5, 3, 4, 19, 56, 34, 17]
print(min(myList))

#return the index of the minimum number in a given list.
def indexOfMin(lyst):
    minIndex = 0
    currentIndex = 1
    while currentIndex < len(lyst):
        #compare the number lyst[minIndex] and lyst[currentIndex].
        #if current is smaller, then reset minIndex to current.
        if lyst[currentIndex] < lyst[minIndex]:
            minIndex = currentIndex
        currentIndex += 1
    return minIndex

print(indexOfMin(myList))