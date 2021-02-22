#import libraries
import numpy as np
import Players

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

    thisarray = []

    #create n variable number of players
    for i in range(num_players):
        thisarray.append(Players.Player("array", i))
    
    return thisarray

        
            

