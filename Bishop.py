import GameBoard
from Blank import Blank
from Piece import Piece


class Bishop(Piece):
    location = ""
    team = '' #Char

    def __init__(self, x, y, t):
        self.location = x + y
        self.team = t



    def move(self, x, y): # X & Y are Destinations
        paths= self.calcPaths()
        coord = x + y
        gameBoard = GameBoard.gb.grid()
        for p in paths:
            if coords == p:
                gameBoard[8 - int(y)][ord(x) - 65] = Bishop(x, y, self.team) # Sets new coordinates to bishop
                gameBoard[8 - int(self.location[1:])][ord(self.location[:1]) - 65] = Blank(x, y) # Sets old coordinates to blank
                GameBoard.gb.grid = gameBoard # Put the board back after editing
                return True
        return False

    def calcPaths(self):
        tempx = ord(self.location[:1])-65 # start to 1
        tempy =  8- int(self.y[1:]) # 1 to end
        posMoves = []
        while(Board.inBounds(tempx + 1, tempy + 1) and GameBoard.gb.grid[tempx + 1][tempy + 1].team == self.team):
            posMoves.append(chr(tempx + 65) + str(8 - tempy))
            tempx +=1
            tempy +=1
            if(not(GameBoard.gb.grid[tempx][tempy].team == self.team and not(GameBoard.gb.grid[tempx][tempy].team == ''))):
                break

        while(Board.inBounds(tempx + 1, tempy - 1) and GameBoard.gb.grid[tempx + 1][tempy - 1].team == self.team):
            posMoves.append(chr(tempx + 65) + str(8 - tempy))
            tempx += 1
            tempy -= 1
            if(not(GameBoard.gb.grid[tempx][tempy].team == self.team and not(GameBoard.gb.grid[tempx][tempy].team == ''))):
                break

        while(Board.inBounds(tempx - 1, tempy + 1) and GameBoard.gb.grid[tempx - 1][tempy + 1].team == self.team):
            posMoves.append(chr(tempx + 65) + str(8 - tempy))
            tempx -= 1
            tempy += 1
            if(not(GameBoard.gb.grid[tempx][tempy].team == self.team and not(GameBoard.gb.grid[tempx][tempy].team == ''))):
                break

        while(Board.inBounds(tempx - 1, tempy - 1) and GameBoard.gb.grid[tempx - 1][tempy - 1].team == self.team):
            posMoves.append(chr(tempx + 65) + str(8 - tempy))
            tempx -= 1
            tempy -= 1
            if(not(GameBoard.gb.grid[tempx][tempy].team == self.team and not(GameBoard.gb.grid[tempx][tempy].team == ''))):
                break

        return [posMoves]


    def toString(self):
        return"B  "







