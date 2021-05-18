import numpy as np
import random
#methods to search for element in given list

#creating array of numbers
array = np.array(np.random.randint(0, 100, size = 20))

#bubblesort array
n = len(array)
for i in range(n-1):
    for j in range(0, n-i-1):
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]

#number to search for
search = np.random.randint(0,100, size = 1)

#///////////Manual search//////////////////////////

#compare search with array
#manual method
for i in range(n):
    if array[i] == search:
        answer = True
    else:
        answer = False

print("Array: ", array,"\nSearch: ", search, 
    "\nFound? --", answer)

#//////////Binary search///////////////////////////
def binary_search(list1, n):
    low = 0  
    high = len(list1) - 1  
    mid = 0  
  
    while low <= high:  
        # for get integer result   
        mid = (high + low) // 2  
  
        # Check if n is present at mid   
        if list1[mid] < n:  
            low = mid + 1  
  
        # If n is greater, compare to the right of mid   
        elif list1[mid] > n:  
            high = mid - 1  
  
        # If n is smaller, compared to the left of mid  
        else:  
            return mid  
  
            # element was not present in the list, return -1  
    return -1  

result  = binary_search(array, search)

print("Array: ", array, "\nSearch: ", search)
if result != -1:
    print("Element is present at index" , str(result))
else:
    print("Element is not present")
