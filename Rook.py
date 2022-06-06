from Blank import Blank
from Piece import Piece
import GameBoard


class Rook(Piece):
    location = ""
    team = ''

    def __init__(self, x, y, t):
        self.location = x + y
        self.team = t

    def move(self, x, y, b):
        paths = self.calcPaths()
        coords = x + y
        gm = b.grid
        for p in paths:
            if coords == p:
                gm[8 - int(y)][ord(x) - 65] = Rook(x, y, self.team)
                location = self.location
                gm[8 - int(location[1:])][ord(location[:1]) - 65] = Blank(x, y)
                b.grid = gm
                return True
            return False

    def calcPaths(self, b):
        loc = self.location
        gm = b
        paths = []
        locx = ord(loc[:1]) - 65
        locy = 8 - int(loc[1:])
        nextx = locx
        nexty = locy - 1
        while(gm.inBounds(nextx, nexty)):
            if(gm.isBlank(nextx, nexty)):
                paths.append(chr(nextx + 65) + str(8 - nexty))
                nexty -= 1
            elif(gm.grid[nexty][nextx].team != self.team):
                paths.append(chr(nextx + 65) + str(8 - nexty))
                break
            else:
                break
        nextx = locx
        nexty = locy + 1
        while(gm.inBounds(nextx, nexty)):
            if(gm.isBlank(nextx, nexty)):
                paths.append(chr(nextx + 65) + str(8 - nexty))
                nexty += 1
            elif(gm.grid[nexty][nexty].team != self.team):
                paths.append(chr(nextx + 65) + str(8 - nexty))
                break
            else:
                break
        nextx = locx - 1
        nexty = locy
        while(gm.inBounds(nextx, nexty)):
            if(gm.inBlank(nextx, nexty)):
                paths.append(chr(nextx + 65) + str(8 - nexty))
                nextx -= 1
            elif(gm.grid[nexty][nextx].team != self.team):
                paths.append(chr(nextx + 65) + str(8 - nexty))
                break
            else:
                break
            nextx = locx + 1
            nexty = locy
            while(gm.inBounds(nextx, nexty)):
                if(gm.isBlank(nextx, nexty)):
                    paths.append(chr(nextx + 65) + str(8 - nexty))
                    nextx += 1
                elif(gm.grid[nexty][nextx].team != self.team):
                    paths.append(chr(nextx + 65) + str(8 - nexty))
                    break
                else:
                    break

        return paths

    def toString(self):
        if (self.team == 'W'):
            return "\033[94mR  \033[0m"
        elif (self.team == 'B'):
            return "\033[93mR  \033[0m"
    