import copy
from Blank import Blank
from Pawn import Pawn
from Queen import Queen
from Rook import Rook
from Knight import Knight
from King import King
from Bishop import Bishop

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
            grid[6][i] = Pawn(chr(i + 65), '2', 'W')
            grid[1][i] = Pawn(chr(i + 65), '7', 'B')

        grid[0][0] = Rook('A','8', 'B') #Black significant Pieces
        grid[0][1] = Knight('B','8', 'B')
        grid[0][2] = Bishop('C','8', 'B')
        grid[0][3] = Queen('D','8', 'B')
        grid[0][4] = King('E','8', 'B')
        grid[0][5] = Bishop('F','8', 'B')
        grid[0][6] = Knight('G','8', 'B')
        grid[0][7] = Rook('H','8', 'B')

        grid[7][0] = Rook('A', '1', 'W') #White's significant Pieces
        grid[7][1] = Knight('B', '1', 'W')
        grid[7][2] = Bishop('C', '1', 'W')
        grid[7][3] = Queen('D', '1', 'W')
        grid[7][4] = King('E', '1', 'W')
        grid[7][5] = Bishop('F', '1', 'W')
        grid[7][6] = Knight('G', '1', 'W')
        grid[7][7] = Rook('H', '1', 'W')
        self.grid = grid

    def print(self):
        grid = self.grid
        col = "8"
        for r in grid:
            row = "\033[92m" + col + "\033[0m "
            for c in r:
                row += c.toString()
            col = str(int(col) - 1)
            print(row)
        print("\033[92m  A  B  C  D  E  F  G  H\033[0m")

    @staticmethod
    def inBounds(x, y):
        return 0 <= x < 8 and 0 <= y < 8

    def isBlank(self, x, y):
        return type(self.grid[y][x]).__name__ == "Blank"


    def isCheck(self, t):
        location = ""
        kingTeam = t
        if(kingTeam == 'B'):
            opTeam = 'W'
        else:
            opTeam = 'B'
        for r in self.grid:
            for c in r:
                if type(c).__name__ == "King" and c.team == kingTeam:
                    location = c.location
        for r in self.grid:
            for c in r:
                if c.team == opTeam:
                    if c.calcPaths(self).count(location) > 0:
                        return True
        return False




    def isCheckmate (self, t):
        if not self.isCheck(t):
            return False
        else:
            kingTeam = t
            if (kingTeam == 'B'):
                opTeam = 'W'
            else:
                opTeam = 'B'
            location = ""
            kingTeam = t
            if (kingTeam == 'B'):
                opTeam = 'W'
            else:
                opTeam = 'B'
            for r in self.grid:
                for c in r:
                    if type(c).__name__ == "King" and c.team == kingTeam: #Finds King
                        location = c.location
            tempBoard = Board()
            for m in (self.grid[ 8 - int(location[1:])][ord(location[:1]) - 65]).calcPaths(self):
                tempBoard.grid = copy.deepcopy(self.grid)
                tempBoard.grid[ 8 - int(location[1:])][ord(location[:1]) - 65].move(m[:1],m[1:], tempBoard)
                if not tempBoard.isCheck(t):
                    return False

            tempBoard = copy.deepcopy(self)
            for r in self.grid:
                for c in r:
                    if c.team == t:
                        for m in c.calcPaths(self):
                            tempBoard.grid = copy.deepcopy(self.grid)
                            c.move(m[:1], m[1:], tempBoard)
                            if not tempBoard.isCheck(t):
                                return False

        return True



