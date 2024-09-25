myList = [12, 2, 4, 3, 7, 9, 26, 18, 29]

def sequentialSearch(target, lyst):
    position = 0
    while position < len(lyst):
        if target == lyst[position]:
            return position
        position += 1

    return -1

print("Index:", sequentialSearch(50, myList))
print("Index", sequentialSearch(7, myList))
print("Index:", sequentialSearch(12, myList))

#Time used for this algorithm
#Best case: Occurs if the target is the first entry in the list.
#Worst case: Occurs if the target is not in the list and every list entry must be compared.
#Average case: n+1 cases
#   1: not i nthe list: n
#   2: the first in the list: 1
#   the second in the list: 2
#   . . . 
#   n: the second last in the list: n-1
#   n+1: the last item in the list: n
# Total number of campirsons / (n+1) = average case.
#Total number of comparisons = n*(n+1) / 2 = O(n/2) = O(n)

# Question: Revise the code to coun the number of comparisons.


myList = [12, 2, 4, 3, 7, 9, 26, 18, 29]

def sequentialSearch(target, lyst):
    position = 0
    comparisons = 0
    while position < len(lyst):
        comparisons += 1
        if target == lyst[position]:
            print("Number of comparisons: ", comparisons)
            return position
        position += 1

    return -1

print("Index:", sequentialSearch(12, myList))
print("Index:", sequentialSearch(29, myList))
print("Index:", sequentialSearch(7, myList))
print("Index:", sequentialSearch(42, myList))
