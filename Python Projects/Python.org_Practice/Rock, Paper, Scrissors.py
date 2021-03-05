
Repeat = 1

while(Repeat == 1):
    print(" Player 1: ")
    print(" Choose 1 for Rock \n Choose 2 for Paper \n Choose 3 for Scissors")
    p1 = int(input("Enter: "))

    #print(p1)

    print(" Player 2: ")
    print(" Choose 1 for Rock \n Choose 2 for Paper \n Choose 3 for Scissors")
    p2 = int(input("Enter: "))

    #print(p2)

    if p1 == 1 and p2 == 1 or p1 == 2 and p2 == 2 or p1 == 3 and p2 == 3:
        print("Game is a tie, play again")
        Repeat = 1
    elif p1 == 2 and p2 == 1 or p1 == 3 and p2 == 2 or p1 == 1 and p2 == 3:
        print("Player 1 Wins")
        Repeat = 0
        choice = int(input("Do you want to play again? Press 1 for yes or 2 for no: "))
        if choice == 1:
            Repeat = 1
    elif p1 == 3 and p2 == 1 or p1 == 1 and p2 == 2 or p1 == 1 and p2 == 3:
        print("Player 2 Wins")
        Repeat = 0
        choice = int(input("Do you want to play again? Press 1 for yes or 2 for no: "))
        if choice == 1:
            Repeat = 1