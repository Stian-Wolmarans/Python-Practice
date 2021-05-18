number = int(input("Type in a interger: "))

if number % 4 == 0:
    print("You inserted a multiple of 4")
elif number % 2 == 0:
    print("You inserted an even number")
elif number % 2 == 1:
    print("You inserted an odd number")

number = int(input("Insert an integer: "))
divide = int(input("Insert integer to divide by: "))

if number % divide == 0:
    print(divide, "divides evenly into", number)
else:
    print(divide, " does not evenly divide into", number)
