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
        for i in(range(8)):
            grid[6][i] = Pawn(chr(i + 65), 2, 'W')
            grid[1][i] = Pawn(chr(i + 65), 7, 'B')

        grid[0,0] = Rook('A',8, 'B') #Black significant Pieces
        grid[0,1] = Knight('B',8, 'B')
        grid[0,2] = Bishop('C',8, 'B')
        grid[0,3] = Queen('D',8, 'B')
        grid[0,4] = King('E',8, 'B')
        grid[0,5] = Bishop('F',8, 'B')
        grid[0,6] = Knight('G',8, 'B')
        grid[0,7] = Rook('H',8, 'B')

        grid[7, 0] = Rook('A', 1, 'W') #White's significant Pieces
        grid[7, 1] = Knight('B', 1, 'W')
        grid[7, 2] = Bishop('C', 1, 'W')
        grid[7, 3] = Queen('D', 1, 'W')
        grid[7, 4] = King('E', 1, 'W')
        grid[7, 5] = Bishop('F', 1, 'W')
        grid[7, 6] = Knight('G', 1, 'W')
        grid[7, 7] = Rook('H', 1, 'W')
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

    def isCheck(self, t):
        location = ""
        kingTeam = t
        if(kingTeam = 'B'):
            opTeam = 'W'
        else:
            opTeam = 'B'
        for r in self.grid:
            for c in r:
                if type(c).__name__ == "King" and c.team == kingTeam:
                    location = c.location


        for r in self.grid
            for c in r:
                if(c.team == opTeam):
                    if c.calcPaths().index(location) >-1:
                        return True
        return False