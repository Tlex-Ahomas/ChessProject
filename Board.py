from Blank import Blank
from Pawn import Pawn
from Queen import Queen

class Board:
    grid = 0

    def __init__(self):
        grid = []
        for r in range(1, 9):
            temp = []
            for c in range(65, 73):
                temp.append(Blank(chr(c), str(r)))
            grid.append(temp)
        grid[6][0] = Pawn('A', '2', 'W')
        grid[5][1] = Pawn('B', '3', 'W')
        self.grid = grid

    def print(self):
        grid = self.grid
        for r in grid:
            row = ""
            for c in r:
                row += c.toString()
            print(row)

    @staticmethod
    def inBounds(x, y):
        return 0 <= x <= 8 and 0 <= y <= 8

    def isBlank(self, x, y):
        return type(self.grid[y][x]).__name__ == "Blank"

    def isCheck(self):
        kingCount = 0
        for r in self.grid:
            for c in r:
                if type(c).__name__ == "King":
                    kingCount += 1
                    kingTeam = c.team
                    tempQueen = Queen(ord(c.location[:1]) - 65, 8 - int(c.location[1:]), kingTeam)
                    area = tempQueen.calcPaths()