#import libraries
import numpy as np
from sklearn.utils import shuffle
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

def reshape(array):
    array = shuffle(array, random_state = 0)
    return array

def pop_n_drop(array1, array2):
    array2[-1] = array1[0]
    array1 = np.delete(array1, 0)
    print(array1)
    print(array2)

    return array2

this1 = np.array([[1,2],[1,5],[9,8]])
this2 = np.array([[4,5],[5,7]])

pop_n_drop(this1,this2)
