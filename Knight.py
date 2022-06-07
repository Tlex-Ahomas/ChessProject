import GameBoard
from Blank import Blank
from Piece import Piece

class Knight (Piece):
    location = ""
    team = '' #Char

    def __init__(self, x, y, t):
        self.location = x + y
        self.team = t


    def move(self, x, y, board):
        paths = self.calcPaths(board) # Gives Valid Paths
        coord = x + y
        gameBoard = board

        for p in paths:
            if p == coord: #If the valid path matches with coordinate intended to move to
                gameBoard.grid[8 - int(y)][ord(x) - 65] = Knight(x, y, self.team) # Sets new coordinates to bishop
                gameBoard.grid[8 - int(self.location[1:])][ord(self.location[:1]) - 65] = Blank(x, y) # Sets old coordinates to blank
                board = gameBoard # Put the board back after editing
                return True
        return False


    def calcPaths(self, board):
        tempx = ord(self.location[:1])-65 # start to 1
        tempy =  8- int(self.location[1:]) # 1 to end
        allXMoves= [2,2, 1, 1, -1, -1, -2, -2]
        allYMoves= [1,-1,2,-2, 2, -2, 1, -1]
        posMoves = []
        for i in(range(8)):
            if(board.inBounds(allXMoves[i] + tempx, allYMoves[i]+tempy) and (board.grid[allYMoves[i] + tempy][allXMoves[i] + tempx].team != self.team )):
                posMoves.append(chr(allXMoves[i] + tempx + 65) + str(8 - (allYMoves[i] + tempy)))
        return posMoves

    def toString(self):
        if (self.team == 'W'):
            return "\033[94mH  \033[0m"
        elif (self.team == 'B'):
            return "\033[93mH  \033[0m"