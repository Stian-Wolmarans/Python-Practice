import numpy as np

#generate 4 digit number
toguess = np.random.randint(0,9, size = 4)

#convert digits to array
b = list(toguess)
c = []

for digit in b:
    c.append (int(digit))

print(c)

#user input 4 digit number
guess = int(input("inter a four digit number: "))

x = list(guess)
y = []

for digit in x:
    y.append(int(digit))

print(y)

#compare strings
#tally score
#output cows or bulls

#prompt to play again

#show final score