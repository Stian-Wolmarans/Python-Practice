import Functions as F
import numpy as np

#build pile of tiles to draw from
pile = F.build_pile()

#get input for number of players
n = int(input("How many players? "))

#create list of player objects
playerlist = F.create_players(n)

#deal 11 tiles to each player
playerlist, pile = F.deal_tiles(playerlist, pile, n)

#check to see if tiles are dealt correctly, none matching the pile
F.confirm_dealtiles(pile, playerlist, n)

#create train objects, number of players + sauce train
trainlist = F.create_trains(n)

#open sauce train
trainlist[-1].set_status(True)

#compare and play functions
for i in range(n):
    if F.compare_n_play(trainlist, playerlist, i)[0] == 0:
        print("Try playing on another train...")
        #function here for player to check open trains
        #function here for picking up a tile if they cannot play
    else:
        playerlist[i].set_array(F.compare_n_play(trainlist,playerlist,i)[2])
    