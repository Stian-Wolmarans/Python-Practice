import Method as M
import numpy as np
import random

game_count = 0

num_players = np.random.randint(1, 8, dtype = int)

for i in range(100):
    M.Play_Game(num_players)
    game_count += 1

print("//////////////////////GAMES PLAYED: ", game_count, "////////////////////")