"""
Tic Tac Toe Player
"""

import math
import copy
from typing import Dict, Any

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


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    #count the number of xs and os and check which is less
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


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    new_moves = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
              new_moves.add((i, j))

    return new_moves

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    #if click on matrix is NOT empty raise exception error

    copy_board = copy.deepcopy(board)

    if copy_board[action[0]][action[1]] != EMPTY:
        raise Exception ("ILLEGAL MOVE")
    else:
        copy_board[action[0]][action[1]] = player(board)

    return copy_board
def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #three moves horizontally, vertically or diagonally
    #vertical
    for i in range(3):
        for j in range(3):
            if board[i][0] == board[i][1] == board[i][2] == X:
                return X
            elif board[i][0] == board[i][1] == board[i][2] == O:
                return O

    for i in range(3):
        for j in range(3):
            if board[0][j] == board[1][j] == board[2][j] == X:
                return X
            elif board[0][j] == board[1][j] == board[2][j] == O:
                return O

    for i in range(3):
        for j in range(3):
            if board[0][0] == board [1][1] == board[2][2] == X:
                return X
            elif board[0][2] == board [1][1] == board[2][0] == X:
                return X
            if board[0][0] == board [1][1] == board[2][2] == O:
                return O
            elif board[0][2] == board [1][1] == board[2][0] == O:
                return O


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #shows either loss, win or draw, when no moves left

    if winner(board) == X or winner(board) == O:
        return True

    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                return False

    else:
        return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return utility(board)

    #if players turn X
    if player(board) == X:
        score = -math.inf
        best_action = None

        for action in actions(board):
            min_val = maxvalue(result(board, action))

            if min_val > score:
                score = min_val
                best_action = action

        return best_action

    elif player(board) == O:
        score = math.inf
        best_action = None

        for action in actions(board):
            max_val = minvalue(result(board, action))

            if max_val < score:
                score = max_val
                best_action = action

        return best_action


def maxvalue(board):

    if terminal(board):
        return utility(board)

     num = -math.inf

    for action in actions(board):
        num = max(num, minvalue(result(board, action)))

    return num


def minvalue(board):

    if terminal(board):
        return utility(board)

    num = math.inf

    for action in actions(board):
        num = min(num, maxvalue(result(board, action)))

    return num





