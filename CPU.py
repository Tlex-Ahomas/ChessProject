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
        self.team = t
        self.difficulty = d # 0 or 1 for now

    def makeSmartMove(self,board):

    def makeMove(self, board):
        if self.difficulty == 0:
            makeBozoMove(board)
        else:
            makeSmartMove(board)


    def makeSmartMove(self,board): #This might take a minute
        tempBoard = copy.deepcopy(board)
        moves = []
        pieces = []
        move = ""
        for r in tempBoard.grid:
            for c in r:
                if(tempBoard.grid[r][c].team == team): #Creates list of pieces CPU can move
                    pieces.appends(tempBoard.grid[r][c])
        r = random.randint(len(pieces))
            while move == "":
                r = random.randint(len(pieces))
                temp = r.calcPaths()
                while len(temp) > 0:
                    r2 = randint(len(temp)




    def makeBozoMove(self, board):
        tempBoard = copy.deepcopy(board)
        moves = []
        pieces = []
        move = ""
        for r in tempBoard.grid:
            for c in r:
                if(c.team == self.team and type(c).__name__ != "Blank"): #Creates list of pieces CPU can move
                    pieces.append(c)
        r = random.randint(0, len(pieces) - 1)
        oldloc = ""
        while(move == ""):
            if r >= len(pieces):
                r = len(pieces) - 1
            print(r)
            temp = self.filterForChecks(tempBoard, pieces[r].location)
            if len(temp) == 0:
                pieces.pop(r)
                r = random.randint(len(pieces))
            else:
                r2 = random.randint(0, len(temp) - 1)
                oldloc = pieces[r].location
                pieces[r].move(temp[r2][:1], temp[r2][1:], tempBoard)
                if type(pieces[r]).__name__ == "Pawn" and ((temp[r2][1:] == '8' and self.team == 'W') or (temp[r2][1:] == '1' and self.team == 'B')):
                    tempBoard.grid[8 - int(temp[r2][1:])][ord(temp[r2][:1]) - 65] = Queen(temp[r2][:1], temp[r2][1:], self.team)
                move = temp[r2]
        return [tempBoard.grid, type(pieces[r]).__name__, oldloc, temp[r2]]


    def filterForChecks(self, board, location):
        tempBoard = copy.deepcopy(board)

        piece = tempBoard.grid[8 - int(location[1:])][ord(location[:1]) - 65]
        moves = piece.calcPaths(tempBoard)
        for m in piece.calcPaths(tempBoard):
            piece.move(m[:1], m[1:], tempBoard)
            if tempBoard.isCheck(self.team):
                moves.remove(m)
            tempBoard = copy.deepcopy(board)
        return moves






