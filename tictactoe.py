"""
Tic Tac Toe Player
"""

import math, copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def count_xos(board):
    """
    Return number of Xs and Os on the board
    """
    counter_x = 0
    counter_o = 0
    for row in board:
        for cell in row:
            if cell == X:
                counter_x += 1   
            elif cell == O:
                counter_o += 1
    return (counter_x, counter_o)

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    counter_x, counter_o = count_xos(board)
    if counter_x > counter_o:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    result = set()
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == EMPTY:
                result.add((i, j))
    return result


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    if board[i][j] != EMPTY:
        raise Exception
    else:
        new_board = copy.deepcopy(board)
        p = player(board)
        new_board[i][j] = p
        return new_board
        
def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check horizontally
    if board[0][0]==X and board[0][1]==X and board[0][2]==X:
        return X
    elif board[0][0]==O and board[0][1]==O and board[0][2]==O:
        return O
    
    elif board[1][0]==X and board[1][1]==X and board[1][2]==X:
        return X
    elif board[1][0]==O and board[1][1]==O and board[1][2]==O:
        return O
    
    elif board[2][0]==X and board[2][1]==X and board[2][2]==X:
        return X
    elif board[2][0]==O and board[2][1]==O and board[2][2]==O:
        return O
    
    # Check vertically
    elif board[0][0]==X and board[1][0]==X and board[2][0]==X:
        return X
    elif board[0][0]==O and board[1][0]==O and board[2][0]==O:
        return O
    
    elif board[0][1]==X and board[1][1]==X and board[2][1]==X:
        return X
    elif board[0][1]==O and board[1][1]==O and board[2][1]==O:
        return O
    
    elif board[0][2]==X and board[1][2]==X and board[2][2]==X:
        return X
    elif board[0][2]==O and board[1][2]==O and board[2][2]==O:
        return O
    
    # Check diagonally
    elif board[0][0]==X and board[1][1]==X and board[2][2]==X:
        return X
    elif board[0][0]==O and board[1][1]==O and board[2][2]==O:
        return O
    
    elif board[0][2]==X and board[1][1]==X and board[2][0]==X:
        return X
    elif board[0][2]==O and board[1][1]==O and board[2][0]==O:
        return O
    
    # If there is no winner
    else:
        return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # if there is a winner
    if winner(board):
        return True
    
    counter_x, counter_o = count_xos(board)
    n = len(board)
    
    # else if the game has ended and there is no empty cell
    if counter_o + counter_x == n*n:
        return True
    else: # else if game has not ended
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    w = winner(board)
    if w == X:
        return 1
    elif w == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
        
    p = player(board)
    if p == X: #X maximizes
        v = float('-inf')
        best_action = None
        for action in actions(board):
            min_value_result = min_value(result(board, action))
            if min_value_result > v:
                v = min_value_result
                best_action = action

    elif p == O: #O minimizes
        v = float('inf')
        best_action = None
        for action in actions(board):
            max_value_result = max_value(result(board, action))
            if max_value_result < v: #The best action is which gives the smallest value
                v = max_value_result
                best_action = action

                
    return best_action

def max_value(board):
    """
    Returns maximum value of a board in this state.
    """
    if terminal(board):
        u = utility(board)
        return u
    
    v = float('-inf')
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
        
    return v

def min_value(board):
    """
    Returns minimum value of a board with this state
    """
    if terminal(board):
        u = utility(board)
        return u
    
    v = float('inf')
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
        
    return v