import numpy as np

num = int(input("Input an integer: "))

prime = 0

for i in range(2,num-1):
    if num % i == 0:
        prime += 1
if prime == 0:
    print("Your number is a prime number")
else:
    print("Your number is not a prime number you dummy")