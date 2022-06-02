from Blank import Blank
from Piece import Piece
import GameBoard


class Rook(Piece):
    location = ""
    team = ''

    def __init__(self, x, y, t):
        self.location = x + y
        self.team = t

    def calcPaths(self):
        loc = self.location
        gm = GameBoard.gb
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
                break;
            else:
                break;

