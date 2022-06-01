from Blank import Blank
from Piece import Piece
import GameBoard


class Pawn(Piece):

    location = ""
    team = ''

    def __init__(self, x, y, t):
        self.location = x + y
        self.team = t

    def move(self, x, y):
        paths = self.calcPaths()
        coords = x + y
        gameBoard = GameBoard.gb.grid
        for p in paths:
            print(p)
            if coords == p:
                gameBoard[8 - int(y)][ord(x) - 65] = Pawn(x, y, self.team)
                location = self.location
                gameBoard[8 - int(location[1:])][ord(location[:1]) - 65] = Blank(x, y)
                GameBoard.gb.grid = gameBoard
                return True
        return False

    def calcPaths(self):
        location = self.location
        paths = []
        gameBoard = GameBoard.gb
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
        return "P  "
