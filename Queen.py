from Blank import Blank
from Piece import Piece
import GameBoard


class Queen(Piece):

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
            if coords == p:
                gameBoard[8 - int(y)][ord(x) - 65] = Queen(x, y, self.team)
                location = self.location
                gameBoard[8 - int(location[1:])][ord(location[:1]) - 65] = Blank(x, y)
                GameBoard.gb.grid = gameBoard
                return True
        return False

    def calcPaths(self):
        loc = self.location
        locx = ord(loc[:1]) - 65
        locy = 8 - int(loc[1:])
        paths = []
        gm = GameBoard.gb
        nextx = locx
        nexty = locy - 1
        while (gm.inBounds(nextx, nexty)):
            if (gm.isBlank(nextx, nexty)):
                paths.append(chr(nextx + 65) + str(8 - nexty))
                nexty -= 1
            elif (gm.grid[nexty][nextx].team != self.team):
                paths.append(chr(nextx + 65) + str(8 - nexty))
                break
            else:
                break
        nextx = locx
        nexty = locy + 1
        while (gm.inBounds(nextx, nexty)):
            if (gm.isBlank(nextx, nexty)):
                paths.append(chr(nextx + 65) + str(8 - nexty))
                nexty += 1
            elif (gm.grid[nexty][nexty].team != self.team):
                paths.append(chr(nextx + 65) + str(8 - nexty))
                break
            else:
                break
        nextx = locx - 1
        nexty = locy
        while (gm.inBounds(nextx, nexty)):
            if (gm.inBlank(nextx, nexty)):
                paths.append(chr(nextx + 65) + str(8 - nexty))
                nextx -= 1
            elif (gm.grid[nexty][nextx].team != self.team):
                paths.append(chr(nextx + 65) + str(8 - nexty))
                break
            else:
                break
        nextx = locx + 1
        nexty = locy
        while (gm.inBounds(nextx, nexty)):
            if (gm.isBlank(nextx, nexty)):
                    paths.append(chr(nextx + 65) + str(8 - nexty))
                    nextx += 1
            elif (gm.grid[nexty][nextx].team != self.team):
                paths.append(chr(nextx + 65) + str(8 - nexty))
                break
            else:
                break
        nextx = locx + 1
        nexty = locy + 1
        while (gm.inBounds(nextx, nexty)):
            if gm.isBlank((nextx, nexty)):
                paths.append(chr(nextx + 65) + str(8 - nexty))
                nextx += 1
                nexty += 1
            elif gm.grid[nexty][nextx].team != self.team:
                paths.append(chr(nextx + 65) + str(8 - nexty))
                break
            else:
                break
        nextx = locx + 1
        nexty = locy - 1
        while gm.inBounds(nextx, nexty):
            if gm.isBlank(nextx, nexty):
                paths.append(chr(nextx + 65) + str(8 - nexty))
                nextx += 1
                nexty -= 1
            elif gm.grid[nexty][nextx].team != self.team:
                paths.append(chr(nextx + 65) + str(8 - nexty))
                break
            else:
                break
        nextx = locx - 1
        nexty = locy + 1
        while gm.inBounds(nextx, nexty):
            if gm.isBlank(nextx, nexty):
                paths.append(chr(nextx + 65) + str(8 - nexty))
                nextx -= 1
                nexty += 1
            elif gm.grid[nexty][nextx].team != self.team:
                paths.append(chr(nextx + 65) + str(8 - nexty))
                break
            else:
                break
        nextx = locx - 1
        nexty = locy - 1
        while gm.inBounds(nextx, nexty):
            if gm.isBlank(nextx, nexty):
                paths.append(chr(nextx + 65) + str(8 - nexty))
                nextx -= 1
                nexty -= 1
            elif gm.grid[nexty][nextx].team != self.team:
                paths.append(chr(nextx + 65) + str(8 - nexty))
                break
            else:
                break

        return paths

    def toString(self):
        return "Q  "
