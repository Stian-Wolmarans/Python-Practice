word = input("Enter a word: ")

array = list(word)

print(array)

n = len(array)
"""
print(n)

print(array[0])
print(array[1])
print(array[2])
"""
"""
if array[0] == array[n-1]:
    print("success")
"""

y = 0
while(y < n):
    if array[y] == array[n-1]:
        x = 0
        y = y + 1
        n = n - 1
    else:
        x = 1
        y = n
if x == 0:
    print("Word is a palindrome")
elif x == 1:
    print("Word is not a palindrome")

print("Done")

