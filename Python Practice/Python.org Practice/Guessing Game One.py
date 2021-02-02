import numpy as np

repeat = 1

while(repeat == 1):

    number = np.random.randint(1,9, size = 1)

    #print(number)

    usernum = int(input("Guess a number from 1-9: "))

    #print(usernum)

    if number == usernum:
        print("You guessed the right number! Do you want to play again \n 1 For Yes \n 2 For No")
        repeat = int(input())
    else:
        print("Your guessed the wrong number :( Do you want to play again \n 1 For Yes \n 2 For No")
        repeat = int(input())