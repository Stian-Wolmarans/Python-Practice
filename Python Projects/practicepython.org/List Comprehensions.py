import numpy as np

array = np.random.randint(0,100, size = 20)

print("First array: ", array)

newarray = []

for i in array:
    if i % 2 == 0:
        newarray.append(i)

print("Array with only even numbers: ", newarray)