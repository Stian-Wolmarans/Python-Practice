import Functions as F

#build pile of tiles to draw from
pile = F.build_pile()

#reorder pile
pile = F.reshape(pile)

#get input for number of players
n = int(input("How many players? "))

#create list of player objects
mylist = F.create_players(n)

#deal out 11 tiles to each player






