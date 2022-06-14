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

    def makeTakeMove(self, board):
        tempboard = copy.deepcopy(board)
        moves = []
        pieces = []
        move = ""
        for r in tempboard.grid:
            for c in r:
                if c.team == self.team and not tempboard.isBlank(ord(c.location[:1]) - 65, 8 - int(c.location[1:])):
                    pieces.append(c)
        p = 0
        while len(pieces) > 0:
            p = random.randint(0, len(pieces) - 1)
            paths = self.filterForChecks(tempboard, pieces[p].location)
            for h in paths:
                if tempboard.grid[8 - int(h[1:])][ord(h[:1]) - 65].team != self.team and not tempboard.isBlank(ord(h[:1]) - 65, 8 - int(h[1:])):
                    move = h
                    oldLoc = pieces[p].location
                    pieces[p].move(move[:1], move[1:], tempboard)
                    if not tempboard.isCheck(self.team):
                        board = copy.deepcopy(tempboard)
                        return [board.grid, type(pieces[p]).__name__, oldLoc, move]
                    else:
                        move = ""
            pieces.pop(p)
        return self.makeBozoMove(board)


    def makeMove(self, board):
        if self.difficulty == 0:
            return self.makeBozoMove(board)
        elif self.difficulty == 1:
            return self.makeSmartMove(board)
        elif self.difficulty == 2:
            return self.makeTakeMove(board)


    def makeSmartMove(self,board): #This might take a minute
        if(team == 'W'):
            otherTeam = 'B'
        else:
            otherTeam = 'W'
        tempBoard = copy.deepcopy(board)
        moves = []
        pieces = []
        enemyPieces = []
        move = ""
        for r in tempBoard.grid:
            for c in r:
                if(c.team == team): #Creates list of pieces CPU can move
                    pieces.appends(c)

        for r in tempBoard.grid:
            for c in r:
                if c.team == otherTeam: #Creates list of enemy pieces
                    pieces.append(c)

        while move == "" and len(pieces>0):
            tempBoard = copy.deepcopy(board)
            r = random.randint(len(pieces))
            oldloc = pieces[r].location
            temp = pieces[r].calcPaths()
            r2 = random.randint(len(temp))
            pieces[r].move(temp[r2][:1], temp[r2][1:], tempBoard)
            while len(temp) > 0:
                r2 = randint(len(temp))
                for p in enemyPieces:
                    for m in enemyPieces.calcPaths(tempBoard):
                         tempBoard2 = copy.deepcopy(tempBoard)  # resets board for further test
                         p.move(m[:1],m[1:])
                         valid = true
                         if tempBoard.isCheck(team) and not tempBoard.isCheck(otherTeam):
                            valid = False
                    if valid == True:
                        move = m
                        return[tempBoard.grid, type(pieces[r]).__name__, oldloc, temp[r2]]
                    else:
                        temp.pop(r2)
                pieces.pop(r)
            makeBozoMove()






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
            temp = self.filterForChecks(tempBoard, pieces[r].location)
            if len(temp) == 0:
                pieces.pop(r)
                r = random.randint(0, len(pieces) - 1)
            else:
                r2 = random.randint(0, len(temp) - 1)
                oldloc = pieces[r].location
                pieces[r].move(temp[r2][:1], temp[r2][1:], tempBoard)
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






