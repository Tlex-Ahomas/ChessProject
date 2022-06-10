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
        r = random.randint(len(pieces))
        while(move == ""):
            temp = filterForChecks(tempBoard, pieces[r].location)
            if len(temp) ==0:
                pieces.pop(r)
            else:
                r2 = randInt(len(temp))
                pieces[r].move(temp[r2])
                move = temp[r2]



        return move

    def filterForChecks(self, board, location):
        tempBoard = copy.deepcopy(board)

        piece = tempBoard.grid[8 - int(location[1:])][ord(location[:1]) - 65]
        moves = piece.calcPaths(tempBoard)
        for m in piece.calcPaths(tempBoard):
            piece.move(m[:1], m[:1], tempBoard)
            if tempBoard.isCheck(team):
                moves.remove(m)
            tempBoard = copy.deepcopy(board)

        return moves






