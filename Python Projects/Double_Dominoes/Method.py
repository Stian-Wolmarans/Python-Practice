import Functions as F
import numpy as np

def Play_Game(players):

    #deal tiles, create players, create pile
    num_players  = players
    pile, playerlist = F.deal_tiles(num_players)

    #create train objects, number of players + sauce train
    trainlist = F.create_trains(num_players)

    #open sauce train
    trainlist[-1].set_status(True)

    #variable to stop game if no one can play
    pass_tally = 0
    count_round = 0

    #play rounds
    while (len(pile) != 0 or pass_tally < num_players+1):
        count_round += 1

        print("/////////////////////ROUND START", count_round, "/////////////////////////////////")

        for i in range(num_players):
            print("//////////////////PLAYER", i, "///////////////////////////////////")
            if F.can_i_play(playerlist, trainlist, i) == 1:

                #play on own train
                F.play_own_train(playerlist, trainlist, i)
                pass_tally = 0

            #if player cannot play on own train
            elif F.can_i_play(playerlist, trainlist, i) == 0:
                print("Can't play")

                #find open trains
                openlist = F.find_open_train(trainlist, num_players)
                print("Open list: ",openlist)

                #if player cannot play
                if F.play_other_train(openlist, trainlist, playerlist, i) == 0:
                    print("Pick up tile from pile...")

                    if len(pile) == 0:
                        pass_tally += 1
                        return

                    #pick up from pile
                    pile = F.pick_up_tile(playerlist, pile, i)[0]
                        
                    print("Opening train...")
                    #open train
                    trainlist[i].set_status(True)
                    pass_tally += 1

                #if player can play on another train
                else:
                    #play on another train
                    F.play_other_train(openlist, trainlist, playerlist, i)
                    pass_tally = 0

            #display player tiles and their trains last tile
            print(playerlist[i].x, len(playerlist[i].x))
            print(trainlist[i].x)

    print("!!!!!!!!!!!!!!!!!!!!!!!GAME END!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("Rounds played: ", count_round)
    print("Tiles left: ", len(pile))
    for i in range(num_players):
        print("Player number: ", i, "Tiles left: ", len(playerlist[i].x))
        