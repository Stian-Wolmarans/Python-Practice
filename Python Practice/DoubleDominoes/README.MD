Program which plays double-dominoes, currently it plays until no player can move and all tiles have been picked up. The algorithm plays clockwise and doesn't employ any strategy into the play style. For instance it will not play on other open trains if it can play on its own train. It will also not consider the best of two/three/etc.. possible moves but will choose the first tile which it can play on its own train and if not start comparing with the next train. The algorithm also doesn't account for the fact that the "Sauce" train can be inserted anywhere in the play order by a player in the first few rounds.

Improvement I could make:
  - Use slicing to manipulate arrays as apposed to array splitting, not sure which one is better optimized...
  - Comments
  - General structure
  - Make algorithm behave strategically
