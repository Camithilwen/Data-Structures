#Python program for implementation of selection sort

A = [64, 25, 12 ,22 ,11]

#Print the original list
print ("Original list of data")
print(A)

#Idea of selection: alwas select the minimum data and put it
#in the beginning of the list. Swap the minimum data with the first
#item in the list

#After the first pass, The list will become
#A = [11, 25, 12 ,22, 64]

#Then start from the second item and repeat the procedure.
#Then start from the third item...
#...
#Continue until reaching the end of the list.

#Traverse through all array elements
for i in range(len(A)-1):

    #Find the minimum element in remaining elements.
    min_indx = i
    for j in range(i+1, len(A)):
        if A[min_indx] > A[j]:
            min_indx = j

    #Swap the found minimum element with the first element.
    A[i], A[min_indx] = A[min_indx], A[i]

    #print out the intermediate result
    print("Iteration ", i)
    print(A)

#Driver code to test above
print ("Sorted array")
print(A)