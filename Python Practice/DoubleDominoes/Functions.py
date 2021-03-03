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
    idx = np.random.randint(1, high = 89, size = 2)
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

def compare_n_play(trainlist, playerlist, player_num):
    
    #flatten arrays
    array1 = trainlist[player_num].x
    array2 = np.hstack(playerlist[player_num].x)

    #compare, play tile on playertrain, delete tile from players hand, return 0 if can't play
    z = 0
    if len(array2) == 0:
        z = 1    
    for q in range(len(array2)):
        if z == 0:
            if array1[0] == array2[q]:
                w = q
                z = 1    
                if w % 2 == 1:
                    np.copyto(array1, array2[w-1], casting = 'same_kind')
                    array2 = np.delete(array2, w-1)
                    array2 = np.delete(array2, w-1)
                if w % 2 == 0:
                    np.copyto(array1, array2[w+1], casting = 'same_kind')
                    array2 = np.delete(array2, w)
                    array2 = np.delete(array2, w)

    #unflatten array and return to 2d
    x = (len(array2)/2)
    array2 = np.array_split(array2, x, axis = 0)
    array2 = np.vstack(array2)


    return z, array1, array2
                 
def find_open_train():

def play_open():

            


