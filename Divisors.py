def divisor():
    array = []
    number = int(input("Type integer: "))
    for i in range(1,number):
        if number % i == 0:
            array.append(i)
    print("Your number is divisable by these numbers: ")
    print(array)

divisor()
            