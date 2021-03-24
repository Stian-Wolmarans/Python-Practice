import Method as M
import numpy as np
import random
import time

game_count = 0

tic = time.perf_counter()

for i in range(10):
    num_players = np.random.randint(2, 8, dtype = int)
    M.Play_Game(num_players)
    game_count += 1

toc = time.perf_counter()
time = toc - tic
print("//////////////////////GAMES PLAYED: ", game_count, "////////////////////")
print("//////////////////////TIME ELAPSED: ", time, "//////////////////////////")
