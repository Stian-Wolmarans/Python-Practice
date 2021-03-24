#import libraries
import numpy as np
from sklearn.utils import shuffle
import Players
import Trains
import random

def deal_tiles(num_players):
        
    #create pile with dimension (1,2)
    pile = np.array([[12,12]])

    #fill pile, new dimension = (91, 2)
    for x in range(13):
        for i in range(x, 13):
            pile = np.append(pile, [[x,i]], axis = 0)

    #remove duplicates  
    pile = np.unique(pile, axis = 0)

    #remove tile 12_12, this tile will be used as starting block
    pile = np.delete(pile, [[90]], axis = 0)

    #shuffle pile
    pile = shuffle(pile, random_state = None)
    pile = shuffle(pile, random_state = 0)
    pile = shuffle(pile, random_state = 1)
    pile = shuffle(pile, random_state = 2)

    #create player list
    thislist = []

    #create players and append to player list
    for i in range(num_players):
        thislist.append(Players.Player("pile", i))

    #loop for each player
    for i in range(num_players):

        #create slice of 11 tiles
        pile_slice = pile[0:11]

        #copy to player    
        np.copyto(thislist[i].x, pile_slice)

        #delete slice from pile
        idx = [0,1,2,3,4,5,6,7,8,9,10]
        pile = np.delete(pile, [[idx]], axis = 0)

    return pile, thislist

def create_trains(num_players):

    thislist = []

    #create n + 1 variable number of trains
    for i in range((num_players + 1)):
        thislist.append(Trains.Train(i, "array", False))
    
    return thislist
                 
def can_i_play(playerlist, trainlist, player_num):
    
    #if hand empty don't play
    if len(playerlist[player_num].x) == 0:
        z = 0
        return z
    
    #flatten arrays
    train = trainlist[player_num].x
    player = np.hstack(playerlist[player_num].x)

    #default train not playable
    z = 0

    #compare 
    for q in range(len(player)):
        if train == player[q]:
            #change playable state
            z = 1
 
    return z

def play_own_train(playerlist, trainlist, player_num):
    
    #flatten arrays
    train = trainlist[player_num].x
    player = np.hstack(playerlist[player_num].x)

    z = 0
    if len(player) != 0:
        for q in range(len(player)):
            if z == 0:
                if train == player[q]:
                    z = 1
                    if q % 2 == 1:
                        trainlist[player_num].set_array(player[q-1])
                        player = np.delete(player, q-1)
                        player = np.delete(player, q-1)
                    if q % 2 == 0:
                        trainlist[player_num].set_array(player[q+1])
                        player = np.delete(player, q)
                        player = np.delete(player, q)
    
    if len(player) > 0:
            
        #unflatten array and return to 2d
        x = (len(player)/2)
        player = np.array_split(player, x, axis = 0)
        player = np.vstack(player)

        #replace player array
        playerlist[player_num].set_array(player)
        
def find_open_train(trainlist, num_players):

    temp = []
    openlist = np.empty_like(temp, dtype=int)

    for i in range(num_players+1):
        if (trainlist[i].get_status()) == True:
            openlist = np.append(openlist, i)

    return openlist

def play_other_train(openlist, trainlist, playerlist, player_num):

    if len(playerlist[player_num].x) == 0:
        z = 0
        return z
    #flatten player array
    player = np.hstack(playerlist[player_num].x)

    #setting loop to only compare with open trains
    #compare with open trains
    z = 0
    for i in (openlist):
        if len(player) != 0:
            for q in range(len(player)):
                if z == 0:
                    if trainlist[i] == player[q]:
                        z = 1
                        #add to open train
                        if q % 2 == 1:
                            trainlist[i].set_array(player[q-1])
                            player = np.delete(player, q-1)
                            player = np.delete(player, q-1)
                        if q % 2 == 0:
                            trainlist[i].set_array(player[q+1])
                            player = np.delete(player, q)
                            player = np.delete(player, q)

    #unflatten array and return to 2d
    x = (len(player)/2)
    player = np.array_split(player, x, axis = 0)
    player = np.vstack(player)

    #replace player array
    playerlist[player_num].set_array(player)

    return z

def pick_up_tile(playerlist, pile, player_num):

    stop = 0

    #append from pile to player
    playerlist[player_num].x = np.append(playerlist[player_num].x, pile[0])

    #delete from pile
    mask = np.ones(len(pile), dtype = bool)
    mask[[0]] = False
    pile = pile[mask]

    
    #unflatten array and return to 2d
    x = (len(playerlist[player_num].x)/2)
    player = np.array_split(playerlist[player_num].x, x, axis = 0)
    player = np.vstack(player)

    #replace player array
    playerlist[player_num].set_array(player)
    
    if len(pile) == 0:
        stop = 1
        print("NO MORE TILES")

    return pile, stop