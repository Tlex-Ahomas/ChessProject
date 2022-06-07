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

    def canCastleLeft(self, b):
        potentialRook = b.grid[8 - int(self.location[1:])][0]
        row = 8 - int(self.location[1:])
        empty = True
        for i in range(1, 4):
            if not b.isBlank(i, row):
                empty = False
        return not(self.moved) and type(potentialRook).__name__ == "Rook" and not potentialRook.moved and empty

    def canCastleRight(self, b):
        row = 8 - int(self.location[1:])
        potentialRook = b.grid[row][7]
        empty = True
        for i in range(5, 7):
            if not b.isBlank(i, row):
                empty = False
        return not(self.moved) and type(potentialRook).__name__ == "Rook" and not potentialRook.moved and empty

    def castle(self, dir, b):
        row = 8 - int(self.location[1:])
        if dir == 'L' and self.canCastleLeft(b):
            #swaps King and Blank
            b.grid[row][2] = b.grid[row][4]
            b.grid[row][4] = Blank(self.location[:1], self.location[1:])

            #swaps Rook and Blank
            b.grid[row][3] = b.grid[row][0]
            b.grid[row][0] = Blank(chr(row + 65), '1')

            #updates location fields of King and Rook
            self.location = "C" + str(8 - row)
            b.grid[row][3] = "D" + str(8 - row)
            return True
        elif dir == 'R' and self.canCastleRight(b):
            #swaps King and Blank
            b.grid[row][6] = b.grid[row][4]
            b.grid[row][4] = Blank("E", str(8 - row))

            #swaps Rook and Blank
            b.grid[row][5] = b.grid[row][7]
            b.grid[row][7] = Blank("H", str(8 - row))

            #updates location fields of King and Rook
            self.location = "G" + str(8 - row)
            b.grid[row][5].location = "F" + str(8 - row)
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