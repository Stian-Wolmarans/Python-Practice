import numpy as np

array = np.random.randint(0, 10, size = 20)

print("Randomly generated array: ")
print(array)

"""print("Values in array that are less than 5: ")
newarray = []
for i in array:
    if i < 5:
        newarray.append(i)
print(newarray)"""

number = int(input("Type an integer to search for: "))
newarray = []

for i in array:
    if i == number:
        newarray.append(i)
print(newarray)
y = 0
for x in newarray:
    if x == number:
        y = y + 1

print("Your number occurs ",y,"times")