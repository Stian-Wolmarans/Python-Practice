import Functions as F
import numpy as np

#build pile of tiles to draw from
pile = F.build_pile()

#shuffle pile
pile = F.reshape(pile)

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
#if player cannot play open train
#close train if player can play on own train

#check left over tiles are loop









