import GameBoard
from Blank import Blank
from Piece import Piece



class King(Piece):
    location = ""
    team = '' #Char
    moved = False

    def __init__(self,x,y,t):
        self.location = x + y
        self.team = t
        self.moved = False

    def move(self, x, y, board):
        paths = self.calcPaths(board) # Gives Valid Paths
        coord = x + y
        gameBoard = board.grid

        for p in paths:
            if p == coord: #If the valid path matches with coordinate intended to move to
                self.moved = True
                oldy = 8 - int(self.location[1:])
                oldx = ord(self.location[:1]) - 65
                gameBoard[8 - int(y)][ord(x) - 65] = gameBoard[oldy][oldx] # Sets new coordinates to King
                self.location = x + y
                gameBoard[oldy][oldx] = Blank(x, y) # Sets old coordinates to blank
                board = gameBoard # Put the board back after editing
                return True
        return False


    def calcPaths(self, board):
        loc = self.location
        tempx = ord(loc[:1]) - 65
        tempy = 8 - int(loc[1:]) #Convert tiles to grid
        paths = []
        allxpaths = [0,1,1,1,0,-1,-1,-1]
        allypaths = [1,1,0,-1,-1,-1,0,1]
        for i in(range(8)):
            if(board.inBounds(allxpaths[i] + tempx, allypaths[i] + tempy) and not(board.grid[allypaths[i] + tempy][allxpaths[i] + tempx].team == self.team )):
                paths.append(chr(allxpaths[i] + tempx + 65) + str(8 - (allypaths[i] + tempy)))
        return paths





    def toString(self):
        if (self.team == 'W'):
            return "\033[94mK  \033[0m"
        elif (self.team == 'B'):
            return "\033[93mK  \033[0m"