myData = [4, 10, 17, 32, 44, 75, 80, 86, 125]

def binarySearch(target, sortedLyst):
    left = 0
    right = len(sortedLyst) - 1
    comparisons = 0

    while left <= right:
        midpoint = (left + right)//2

        if target == sortedLyst[midpoint]:
            return midpoint
        elif target < sortedLyst[midpoint]:
            right = midpoint - 1
        else :
            left = midpoint + 1

    return -1

print("Index: ", binarySearch(2, myData))
print("Index: ", binarySearch(17, myData))

# Revise the code to count the number of comparisons.

myData = [4, 10, 17, 32, 44, 75, 80, 86, 125]

def binarySearch(target, sortedLyst):
    left = 0
    right = len(sortedLyst) - 1
    comparisons = 0

    #declare a counter
    count = 0
    while left <= right:
        midpoint = (left + right)//2
        count += 1
        if target == sortedLyst[midpoint]:
            print("Number of comparisons: ", count) #before return,
            return midpoint
        elif target < sortedLyst[midpoint]:
            right = midpoint - 1
        else :
            left = midpoint + 1

    return -1

print("Index: ", binarySearch(2, myData))
print("Index: ", binarySearch(17, myData))
print("Index: ", binarySearch(44, myData))
print("Index: ", binarySearch(4, myData))
print("Index: ", binarySearch(125, myData))







