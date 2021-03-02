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
    return array

def deal_tiles(players, pile, num_players):

    #remove three random tiles
    idx = np.random.randint(0, high = 89, size = 2)
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
        
    #reinsert three removed tiles
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

def compare(trainlist, playerlist, player_num):
    trainlist[player_num].x = np.vstack(trainlist[player_num].x)
    print(trainlist[player_num].x)

    playerlist[player_num].x = np.vstack(playerlist[player_num].x)
    print(playerlist[player_num].x)


