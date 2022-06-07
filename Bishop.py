import GameBoard
from Blank import Blank
from Piece import Piece


class Bishop(Piece):
    location = ""
    team = '' #Char

    def __init__(self, x, y, t):
        self.location = x + y
        self.team = t



    def move(self, x, y, board): # X & Y are Destinations
        paths= self.calcPaths(board)
        coord = x + y
        gameBoard = board.grid
        for p in paths:
            if coord == p:
                gameBoard[8 - int(y)][ord(x) - 65] = Bishop(x, y, self.team) # Sets new coordinates to bishop
                gameBoard[8 - int(self.location[1:])][ord(self.location[:1]) - 65] = Blank(x, y) # Sets old coordinates to blank
                board.grid = gameBoard # Put the board back after editing
                return True
        return False

    def calcPaths(self, board):
        tempx = ord(self.location[:1])-65 # start to 1
        tempy =  8- int(self.location[1:]) # 1 to end
        posMoves = []
        while(board.inBounds(tempx + 1, tempy + 1) and board.grid[tempy + 1][tempx + 1].team != self.team):
            posMoves.append(chr((tempx + 1) + 65) + str(8 - (tempy + 1)))
            tempx +=1
            tempy +=1
            if(not(board.grid[tempy][tempx].team == self.team and not(board.grid[tempy][tempx].team == ''))):
                break

        tempx = ord(self.location[:1]) - 65  # start to 1
        tempy = 8 - int(self.location[1:])  # 1 to end
        while(board.inBounds(tempx + 1, tempy - 1) and board.grid[tempy - 1][tempx + 1].team != self.team):
            posMoves.append(chr((tempx + 1) + 65) + str(8 - (tempy - 1)))
            tempx += 1
            tempy -= 1
            if(not(board.grid[tempy][tempx].team == self.team) and not(board.grid[tempy][tempx].team == '')):
                break

        tempx = ord(self.location[:1]) - 65  # start to 1
        tempy = 8 - int(self.location[1:])  # 1 to end
        while(board.inBounds(tempx - 1, tempy + 1) and board.grid[tempy + 1][tempx - 1].team != self.team):
            posMoves.append(chr((tempx - 1) + 65) + str(8 - (tempy + 1)))
            tempx -= 1
            tempy += 1
            if not(board.grid[tempy][tempx].team == self.team) and not(board.grid[tempy][tempx].team == ''):
                break

        tempx = ord(self.location[:1]) - 65  # start to 1
        tempy = 8 - int(self.location[1:])  # 1 to end
        while board.inBounds(tempx - 1, tempy - 1) and board.grid[tempy - 1][tempx - 1].team != self.team:
            posMoves.append(chr((tempx - 1) + 65) + str(8 - (tempy - 1)))
            tempx -= 1
            tempy -= 1
            if not(board.grid[tempy][tempx].team == self.team) and not(board.grid[tempy][tempx].team == ''):
                break

        return posMoves


    def toString(self):
        if (self.team == 'W'):
            return "\033[94mB  \033[0m"
        elif (self.team == 'B'):
            return "\033[93mB  \033[0m"







