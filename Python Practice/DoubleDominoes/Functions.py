#import libraries
import numpy as np
from sklearn.utils import shuffle
import Players
import Trains
import random

def build_pile():

    #create array
    pile = np.array([[12,12]])

    #fill array
    for x in range(13):
        for i in range(x, 13):
            pile = np.append(pile, [[x,i]], axis = 0)

    #remove duplicate 00  
    pile = np.unique(pile, axis = 0)
    return pile

def create_players(num_players):

    thislist = []

    #create n variable number of players
    for i in range(num_players):
        thislist.append(Players.Player("array", i))
    
    return thislist

def reshape(array):
    array = shuffle(array, random_state = None)
    array = shuffle(array, random_state = 0)
    array = shuffle(array, random_state = 1)
    array = shuffle(array, random_state = 2)
    return array

def deal_tiles(players, pile, num_players):

    #remove three random tiles
    idx = np.random.randint(1, high = 88, size = 2)
    tempstore = pile[tuple([idx])]
    pile = np.delete(pile, [[90]], axis = 0)
    pile = np.delete(pile, [[idx]], axis = 0)
   
    #shuffle pile
    for i in range(5):
        pile = reshape(pile)
   
    #split
    pile = np.array_split(pile, 8, axis = 0)

    #copy to player arrays
    for i in range(num_players):
        temp = pile[i]  
        np.copyto(players[i].x, temp) 
    
    #create new pile(right side of split)
    pile = np.vstack(pile)  
    n = (num_players*11)
    mask = np.ones(len(pile), dtype = bool)
    for i in range(n):
        mask[[i]] = False
        newpile = pile[mask]
        
    #reinsert two removed removed tiles
    newpile = np.append(newpile, tempstore, axis = 0)

    return players, newpile

def confirm_dealtiles(pile, mylist, num_players):

    s = 1
    for y in range(num_players):
        if mylist[y].x.any == pile.any:
            s = 0
    if s == 1:
        print("Tiles dealt: Success")
    else:
        print("Tiles not dealt correctly")

def create_trains(num_players):

    thislist = []

    #create n + 1 variable number of trains
    for i in range((num_players + 1)):
        thislist.append(Trains.Train(i, "array", False))
    
    return thislist
                 
def can_i_play(playerlist, trainlist, player_num):

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

    print("Picking up tile...")
    print("Length pile: ", len(pile))

    #append from pile to player
    playerlist[player_num].x = np.append(playerlist[player_num].x, pile[0])
    print("After pick up: ", playerlist[player_num].x)
    print("Length player array: ", len(playerlist[player_num].x))

    #delete from pile
    print("Length Pile: ", len(pile))
    mask = np.ones(len(pile), dtype = bool)
    mask[[0]] = False
    pile = pile[mask]
    print("Length Pile: ", len(pile))

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