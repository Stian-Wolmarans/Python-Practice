import numpy as np

array1 = np.random.randint(0, 10, size = 20)
array2 = np.random.randint(0, 10, size = 30)

array3 = []

print(array1)
print(array2)

for i in array1:
    for x in array2:
        if array1[i] == array2[x]:
            array3.append(i)
print("The matching values in these lists are: ")
array3 = list(dict.fromkeys(array3))

#bubble sort
n = len(array3)
for x in range(n-1):
    for j in range(0,n-x-1):
        if array3[j] > array3[j+1]:
            array3[j], array3[j+1] = array3[j+1],array3[j]
    
print(array3)


