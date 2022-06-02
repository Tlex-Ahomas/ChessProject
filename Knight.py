import GameBoard
from Blank import Blank
from Piece import Piece

class Knight (Piece):
    location = ""
    team = '' #Char

    def __init__(self, x, y, t):
        location = x + y
        team = t


    def move(self, x, y):
        paths = self.calcPaths() # Gives Valid Paths
        coord = x + y
        gameBoard = GameBoard.gb.grid

        for p in paths:
            if p == coord: #If the valid path matches with coordinate intended to move to
                gameBoard[8 - int(y)][ord(x) - 65] = Knight(x, y, self.team) # Sets new coordinates to bishop
                gameBoard[8 - int(self.location[1:])][ord(self.location[:1]) - 65] = Blank(x, y) # Sets old coordinates to blank
                GameBoard.gb.grid = gameBoard # Put the board back after editing
                return True
        return False


    def calcPaths(self):
        tempx = ord(self.location[:1])-65 # start to 1
        tempy =  8- int(self.y[1:]) # 1 to end
        allXMoves= [2,2, 1, 1, -1, -1, -2, -2]
        allYMoves= [1,-1,2,-2, 2, -2, 1, -1]
        posMoves = []
        for i in(range(8)):
            if(GameBoard.gb.inBounds(allXMoves[i], allYMoves[i] and not(GameBoard.gb.grid[allXMoves[i]][allYMoves[i]] == self.team ))):
                posMoves.append(chr(allXMoves[i] + 65) + str(8 - allYMoves[i]))
        return posMoves

    def toString(self):
        return "H  "