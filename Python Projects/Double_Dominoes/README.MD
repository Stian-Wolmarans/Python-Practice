Program which plays double-dominoes, currently it plays until no player can move and all tiles have been picked up. The algorithm plays clockwise and doesn't employ any strategy into the play style. For instance it will not play on other open trains if it can play on its own train. It will also not consider the best of two/three/etc.. possible moves but will choose the first tile which it can play on its own train and if not start comparing with the next train. The algorithm also doesn't account for the fact that the "Sauce" train can be inserted anywhere in the play order by a player in the first few rounds.

**Update 1:**
Packaged whole game into one method in order to play batches of games. Currently game can play between 10 - 100 games before an error occurs. Most bugs came up when player hands or pile were empty so I added some conditional statements to exit functions, thought the condition in the main methods would do the trick but apperently not. Still encountering an error when dealing tiles. In some games there seems to be an un-equal split in dividing the tiles up into sets of 11. Will create fork to attempt to rewrite the function. Will try using slicing instead of array split. Had not heard of array slicing prior to this. Currently train tiles are not stored in train but only the last placed tile is remembered,I did this because that was all that was needed to compare which trains are playable. For a visual representation it would be cool to see the whole train. 

**Update 2:**
Merged deal_tiles, create_pile, and create_players into one function which uses simpler code, for instance slicing instead of splitting. Tried to reduce iterations where possible. Managed to let a 1000+ games run without any errors. Every game is roughly 0.2-0.4 seconds. Would be coool to reduce this time. 

**Improvements:**
  - "Sauce Train" varaible placement   
  - Improve Comments
  - Make algorithm behave strategically
  - Allow all played tiles to be stored in train array, not just last train tile
  - Create a visual representation of the game 
