from Blank import Blank
from Piece import Piece
from Queen import Queen
from Rook import Rook
from Knight import Knight
from Bishop import Bishop
import GameBoard


class Pawn(Piece):

    location = ""
    team = ''

    def __init__(self, x, y, t):
        self.location = x + y
        self.team = t


    def move(self, x, y, b):
        paths = self.calcPaths(b)
        coords = x + y
        gameBoard = b.grid
        for p in paths:
            if coords == p:
                gameBoard[8 - int(y)][ord(x) - 65] = Pawn(x, y, self.team)
                location = self.location
                gameBoard[8 - int(location[1:])][ord(location[:1]) - 65] = Blank(x, y)
                b.grid = gameBoard
                if (self.team == 'W' and y == "8") or (self.team == 'B' and y == "1"):
                    b.print()
                    ans = input("You can promote your pawn, options: Q for Queen, R for Rook, B for Bishop, K for Knight ")
                    while not(ans == "Q" or ans == "R" or ans == "B" or ans == "K"):
                        ans = input("Invalid input, options: Q for Queen, R for Rook, B for Bishop, K for Knight ")
                    if ans == "Q":
                        gameBoard[8 - int(y)][ord(x) - 65] = Queen(x, y, self.team)
                    elif ans == "R":
                        gameBoard[8 - int(y)][ord(x) - 65] = Rook(x, y, self.team)
                    elif ans == "B":
                        gameBoard[8 - int(y)][ord(x) - 65] = Bishop(x, y, self.team)
                    elif ans == "K":
                        gameBoard[8 - int(y)][ord(x) - 65] = Knight(x, y, self.team)
                    b.grid = gameBoard
                return True
        return False

    def calcPaths(self, b):
        location = self.location
        paths = []
        gameBoard = b
        nextx = ord(location[:1]) - 65
        nexty = 0
        addMove = 0
        if self.team == 'W':
            nexty = (8 - int(location[1:])) - 1
            addMove = -1
        else:
            nexty = (8 - int(location[1:])) + 1
            addMove = 1
        if gameBoard.inBounds(nextx, nexty) and gameBoard.isBlank(nextx, nexty):
            paths.append(chr(nextx + 65) + str(8 - nexty))
        if int(location[1:]) == 2 and self.team == 'W' or int(location[1:]) == 7 and self.team == 'B':
            nexty += addMove
            if gameBoard.inBounds(nextx, nexty) and gameBoard.isBlank(nextx, nexty):
                paths.append(chr(nextx + 65) + str(8 - nexty))
            nexty -= addMove
        nextx -= 1
        if gameBoard.inBounds(nextx, nexty) and not gameBoard.isBlank(nextx, nexty) and gameBoard.grid[nexty][nextx].team != self.team:
            paths.append(chr(nextx + 65) + str(8 - nexty))
        nextx += 2
        if gameBoard.inBounds(nextx, nexty) and not gameBoard.isBlank(nextx, nexty) and gameBoard.grid[nexty][nextx].team != self.team:
            paths.append(chr(nextx + 65) + str(8 - nexty))

        return paths

    def toString(self):
        if(self.team == 'W'):
            #return "\033[94mP  \033[0m"
            return "\u265F  "
        elif(self.team == 'B'):
            #return "\033[93mP  \033[0m"
            return "\u2659  "
