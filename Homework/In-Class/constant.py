
def sumUp(n):
    #add everything from 1 to n
    sum = 0
    for number in range(n+1):
        sum += n
        #print(sum)
    return sum

print(sumUp(10))
#O(n+1) = O(n) Linear running time.

def sumUp(n):
    return n*(n+1)/2

print(sumUp(10))
#running time O(1), constant running time