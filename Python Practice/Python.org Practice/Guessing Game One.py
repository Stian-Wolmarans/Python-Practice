import numpy as np

repeat = 1
guesses = 0
correct = 0
incorrect = 0

while(repeat == 1):

    number = np.random.randint(1,5, size = 1)

    #print(number)

    usernum = int(input("Guess a number from 1-5: "))

    #print(usernum)

    if number == usernum:
        print("You guessed the right number! Do you want to play again \n 1 For Yes \n 2 For No")
        repeat = int(input())
        guesses += 1
        correct += 1
    else:
        print("Your guessed the wrong number :( Do you want to play again \n 1 For Yes \n 2 For No")
        repeat = int(input())
        guesses += 1
        incorrect += 1
print(" Giving up so soon? Here are your results: ")
print(" Guesses = ", guesses, "\n Correct = ", correct, "\n Incorrect = ", incorrect)

