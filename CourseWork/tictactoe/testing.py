import math

X = "X"
O = "O"
EMPTY = None

def IsWinningSet(inputSet):

    winSets = (((0,0),(0,1),(0,2)), ((1,0),(1,1),(1,2)), 
    ((2,0),(2,1),(2,2)), ((0,0),(1,0),(2,0)), 
    ((0,1),(1,1),(2,1)), ((0,2),(1,2),(2,2)), 
    ((0,0),(1,1),(2,2)), ((2,0),(1,1),(0,2)))

    winBigSet = set(frozenset(i) for i in winSets)

    for i in winBigSet:
        if i.intersection(inputSet) == i:
            return True
    return False


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def terminal(board):
    """
    Returns true if game is over
    """
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False    
    return True


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    xcount = 0
    ocount = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                xcount += 1
            elif board[i][j] == O:
                ocount += 1
    if xcount > ocount:
        return O
    else:
        return X


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    move = EMPTY

    #check player turn
    if player(board) == X:
        move = X
    elif player(board) == O:
        move = O  

    #move
    board[action[0]][action[1]] = move
    return board


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_moves = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_moves.add((i,j))
    return possible_moves


def winner(board):
    """
    Returns the winner of the game, if there is one
    """
    #Collect values for played on tiles
    xplacements = set()
    oplacements = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                xplacements.add((i,j))
            if board[i][j] == O:
                oplacements.add((i,j))    

    #Check for winner or return none if no winner
    if IsWinningSet(oplacements):
        return O
    elif IsWinningSet(xplacements):
        return X
    else:
        return None


def utility(board):
    if winner(board) == O:
        return -1
    elif winner(board) == X:
        return 1
    else:
        return 0


def MinValue(board):
    v = float('-inf') 
    
    if terminal(board):
        return utility(board)
    
    for action in actions(board):
        v = max(v, MinValue(result(board, action)))
    return v

def MaxValue(board):
    v = float('inf') 
    
    if terminal(board):
        return utility(board)
    
    for action in actions(board):
        v = min(v, MaxValue(result(board, action)))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board) == X:
        v = float('-inf')
        move = None

        for action in actions(board):
            min_val = MinValue(result(board, action))
            if min_val > v:
                v = min_val
                move = action
        return move
    elif player(board) == O:
        v = float('inf')
        move = None

        for action in actions(board):
            max_val = MaxValue(result(board, action))
            if max_val < v:
                v = max_val
                move = action
        return move


#play game
game_board = initial_state()

def playgame():
    print(game_board)
    player(game_board)
    action = minimax(game_board)
    result(game_board, action)
    print(game_board)

playgame()

