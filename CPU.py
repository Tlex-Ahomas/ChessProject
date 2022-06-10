import copy #copy.deepcopy
import random
from Blank import Blank
from Pawn import Pawn
from Queen import Queen
from Rook import Rook
from Knight import Knight
from King import King
from Bishop import Bishop

class CPU:
    team = ''
    difficulty = 0

    def __init__(self, t, d):
        team = t
        difficulty = d # 0 or 1 for now


    def makeMove(self, board):
        tempBoard = copy.deepcopy(board)
        moves = []
        pieces = []
        move = ""
        for r in tempBoard.grid:
            for c in r:
                if(tempBoard.grid[r][c].team == team): #Creates list of pieces CPU can move
                    pieces.appends(tempBoard.grid[r][c])


        return move

    def filterForChecks(self, board, location):
        return 0 #temporary



