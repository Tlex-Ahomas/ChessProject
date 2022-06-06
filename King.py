import GameBoard
from Blank import Blank
from Piece import Piece



class King(Piece):
    location = ""
    team = '' #Char

    def __init__(self,x,y,t):
        location = x + y
        team = t

    def move(self, x, y):
        paths = self.calcPaths() # Gives Valid Paths
        coord = x + y
        gameBoard = GameBoard.gb.grid

        for p in paths:
            if p == coord: #If the valid path matches with coordinate intended to move to
                gameBoard[8 - int(y)][ord(x) - 65] = King(x, y, self.team) # Sets new coordinates to bishop
                gameBoard[8 - int(self.location[1:])][ord(self.location[:1]) - 65] = Blank(x, y) # Sets old coordinates to blank
                GameBoard.gb.grid = gameBoard # Put the board back after editing
                return True
        return False


    def calcPaths(self):
        loc = self.location
        tempx = ord(loc[:1]) - 65
        tempx = 8 - int(loc[1:]) #Convert tiles to grid
        paths = []
        allxpaths = [0,1,1,1,0,-1,-1,-1]
        allypaths = [1,1,0,-1,-1,-1,0,1]
        for i in(range(8)):
            if(GameBoard.gb.inBounds(allxpaths[i] + tempx, allypaths[i] + tempy) and not(GameBoard.gb.grid[allXMoves[i]][allYMoves[i]] == self.team )):
                paths.append(chr(allXMoves[i] + tempx + 65) + str(8 - (allYMoves[i] + tempy)))
        return paths





    def toString(self):
        return "K  "