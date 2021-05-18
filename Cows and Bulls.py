import numpy as np

Bull = 0
Cow = 0
again = 1

toguess = np.random.randint(0,9, size = 4)


while(again == 1):
    smallCow = 0
    smallBull = 0

    #generate 4 digit number
    #toguess = np.random.randint(0,9, size = 4)
    #print(toguess)

    #convert digits to list
    b = list(toguess)
    c = []
    for digit in b:
        c.append (int(digit))
    #print(c)

    #user input 4 digit number
    guess1 = int(input("Enter a digit: "))

    #convert to list
    x = [int(t) for t in str(guess1)]
    #print (x)

    #compare strings x and c for cows
    for t in range(len(x)):
        if c[t] == x[t]:
            smallCow += 1
            Cow += 1
    print("You scored", smallCow, "Cows!")

    #compare string x and c for bulls
    array3 = []
    for y in range(len(x)):
        for z in range(len(c)):
            if x[y] == c[z]:
                array3.append(x[y])
    array3 = list(dict.fromkeys(array3))
    #print(array3)
    n = len(array3)
    smallBull += n
    smallBull = smallBull - smallCow
    Bull += n
    print("You scored", smallBull, "Bulls!")

    #prompt to play again    
    #if toguess == guess1:
     #   again = 0

#show final score
print("Your final score is", Bull, "Bulls and", Cow, "Cows")


