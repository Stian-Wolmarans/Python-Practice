import Functions as F
import numpy as np

#build pile of tiles to draw from
pile = F.build_pile()

#reorder pile
pile = F.reshape(pile)

#get input for number of players
n = int(input("How many players? "))

#create list of player objects
mylist = F.create_players(n)

#remove three tiles
i = np.random.randint(0,7)
pile = np.delete(pile, [[i,(i+2)],[i,(i+3)]], axis = 0)

#deal 11 tiles to each player
for i in range(n):
    mylist[i].set_array(F.split_n_copy(mylist[i].get_array(), pile, i))

#create train objects, number of players + sauce train







