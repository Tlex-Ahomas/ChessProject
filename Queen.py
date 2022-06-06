from Blank import Blank
from Piece import Piece
import GameBoard


class Queen(Piece):

    location = ""
    team = ''

    def __init__(self, x, y, t):
        self.location = x + y
        self.team = t

    def move(self, x, y, board):
        paths = self.calcPaths(board)
        coords = x + y
        gameBoard = board.grid
        for p in paths:
            if coords == p:
                gameBoard[8 - int(y)][ord(x) - 65] = Queen(x, y, self.team)
                location = self.location
                gameBoard[8 - int(location[1:])][ord(location[:1]) - 65] = Blank(x, y)
                board.grid = gameBoard
                return True
        return False

    def calcPaths(self, board):
        loc = self.location
        locx = ord(loc[:1]) - 65
        locy = 8 - int(loc[1:])
        paths = []
        nextx = locx
        nexty = locy - 1
        while (board.inBounds(nextx, nexty)):
            if (board.isBlank(nextx, nexty)):
                paths.append(chr(nextx + 65) + str(8 - nexty))
                nexty -= 1
            elif (board.grid[nexty][nextx].team != self.team):
                paths.append(chr(nextx + 65) + str(8 - nexty))
                break
            else:
                break
        nextx = locx
        nexty = locy + 1
        while (board.inBounds(nextx, nexty)):
            if (board.isBlank(nextx, nexty)):
                paths.append(chr(nextx + 65) + str(8 - nexty))
                nexty += 1
            elif (board.grid[nexty][nexty].team != self.team):
                paths.append(chr(nextx + 65) + str(8 - nexty))
                break
            else:
                break
        nextx = locx - 1
        nexty = locy
        while (board.inBounds(nextx, nexty)):
            if (board.inBlank(nextx, nexty)):
                paths.append(chr(nextx + 65) + str(8 - nexty))
                nextx -= 1
            elif (board.grid[nexty][nextx].team != self.team):
                paths.append(chr(nextx + 65) + str(8 - nexty))
                break
            else:
                break
        nextx = locx + 1
        nexty = locy
        while (board.inBounds(nextx, nexty)):
            if (board.isBlank(nextx, nexty)):
                    paths.append(chr(nextx + 65) + str(8 - nexty))
                    nextx += 1
            elif (board.grid[nexty][nextx].team != self.team):
                paths.append(chr(nextx + 65) + str(8 - nexty))
                break
            else:
                break
        nextx = locx + 1
        nexty = locy + 1
        while (board.inBounds(nextx, nexty)):
            if board.isBlank((nextx, nexty)):
                paths.append(chr(nextx + 65) + str(8 - nexty))
                nextx += 1
                nexty += 1
            elif board.grid[nexty][nextx].team != self.team:
                paths.append(chr(nextx + 65) + str(8 - nexty))
                break
            else:
                break
        nextx = locx + 1
        nexty = locy - 1
        while board.inBounds(nextx, nexty):
            if board.isBlank(nextx, nexty):
                paths.append(chr(nextx + 65) + str(8 - nexty))
                nextx += 1
                nexty -= 1
            elif board.grid[nexty][nextx].team != self.team:
                paths.append(chr(nextx + 65) + str(8 - nexty))
                break
            else:
                break
        nextx = locx - 1
        nexty = locy + 1
        while board.inBounds(nextx, nexty):
            if board.isBlank(nextx, nexty):
                paths.append(chr(nextx + 65) + str(8 - nexty))
                nextx -= 1
                nexty += 1
            elif board.grid[nexty][nextx].team != self.team:
                paths.append(chr(nextx + 65) + str(8 - nexty))
                break
            else:
                break
        nextx = locx - 1
        nexty = locy - 1
        while board.inBounds(nextx, nexty):
            if board.isBlank(nextx, nexty):
                paths.append(chr(nextx + 65) + str(8 - nexty))
                nextx -= 1
                nexty -= 1
            elif board.grid[nexty][nextx].team != self.team:
                paths.append(chr(nextx + 65) + str(8 - nexty))
                break
            else:
                break

        return paths

    def toString(self):
        if (self.team == 'W'):
            return "\033[94mQ  \033[0m"
        elif (self.team == 'B'):
            return "\033[93mQ  \033[0m"
