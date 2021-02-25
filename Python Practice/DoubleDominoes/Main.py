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

#deal 11 tiles to each player
for x in range(n):
    mylist[x].set_array(F.split_n_copy(mylist[x].get_array(), pile, x))

#delete dealt tiles form pile

#replace randomly removed tiles

#create train objects, number of players + sauce train

#compare and play functions

#check left over tiles are loop

print(mylist[0].x)







