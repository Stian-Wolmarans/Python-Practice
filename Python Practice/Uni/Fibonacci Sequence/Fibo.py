myarray = [0,1]
n = int(input("Enter a number for sequence: "))
x = 0
while x < n:
    y = myarray[x] + myarray[x+1]
    myarray.append(y)
    x = x + 1
print(myarray)


