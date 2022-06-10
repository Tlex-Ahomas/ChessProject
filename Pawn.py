from Blank import Blank
from Piece import Piece
from Queen import Queen
from Rook import Rook
from Knight import Knight
from Bishop import Bishop


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
                enpassant = False
                if x != self.location[:1] and type(gameBoard[8 - int(y)][ord(x) - 65]).__name__ == "Blank":
                    enpassant = True
                gameBoard[8 - int(y)][ord(x) - 65] = Pawn(x, y, self.team)
                location = self.location
                if enpassant:
                    gameBoard[8 - int(location[1:])][ord(x) - 65] = Blank(x, location[1:])
                gameBoard[8 - int(location[1:])][ord(location[:1]) - 65] = Blank(location[:1], location[1:])
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
        oppTeam = ''
        nextx = ord(location[:1]) - 65
        nexty = 0
        addMove = 0
        if self.team == 'W':
            nexty = (8 - int(location[1:])) - 1
            addMove = -1
            oppTeam = 'B'
        else:
            nexty = (8 - int(location[1:])) + 1
            addMove = 1
            oppTeam = 'W'

        if gameBoard.inBounds(nextx, nexty) and gameBoard.isBlank(nextx, nexty):
            paths.append(chr(nextx + 65) + str(8 - nexty))

        if int(location[1:]) == 2 and self.team == 'W' or int(location[1:]) == 7 and self.team == 'B':
            nexty += addMove
            if gameBoard.inBounds(nextx, nexty) and gameBoard.isBlank(nextx, nexty):
                paths.append(chr(nextx + 65) + str(8 - nexty))
            nexty -= addMove


        oppMoves = []
        if self.team == 'W':
            oppMoves = gameBoard.moveListB
        else:
            oppMoves = gameBoard.moveListW
        lastMoveDiff = 0
        lastMove = ""
        currPos = ""
        potPawn = Blank('A', '1')
        lastPiece = ""
        if len(oppMoves) > 0:
            lastMove = oppMoves[len(oppMoves) - 1]
            if lastMove.index(" ") > 0:
                lastMoveDiff = abs(int(lastMove[lastMove.index(" ") - 1 : lastMove.index(" ")]) - int(lastMove[lastMove.index(" ") + 2 :]))
                lastPiece = lastMove[:lastMove.index("-")]
                currPos = lastMove[lastMove.index(" ")]
        nextx -= 1
        if gameBoard.inBounds(nextx, 8 - int(location[1:])):
            potPawn = gameBoard.grid[8 - int(location[1:])][nextx]

        if (gameBoard.inBounds(nextx, nexty) and not gameBoard.isBlank(nextx, nexty) and gameBoard.grid[nexty][nextx].team != self.team) or (type(potPawn).__name__ == "Pawn" and potPawn.team == oppTeam and lastPiece == "Pawn" and potPawn.location == currPos and lastMoveDiff == 2):
            paths.append(chr(nextx + 65) + str(8 - nexty))

        potPawn = Blank('A', '1')
        lastMoveDiff = 0
        lastMove = ""
        currPos = ""
        lastPiece = ""
        if len(oppMoves) > 0:
            lastMove = oppMoves[len(oppMoves) - 1]
            if lastMove.index(" ") > 0:
                lastMoveDiff = abs(int(lastMove[lastMove.index(" ") - 1: lastMove.index(" ")]) - int(lastMove[lastMove.index(" ") + 2:]))
                lastPiece = lastMove[:lastMove.index("-")]
                currPos = lastMove[lastMove.index(" ") + 1:]
        nextx += 2
        if gameBoard.inBounds(nextx, 8 - int(location[1:])):
            potPawn = gameBoard.grid[8 - int(location[1:])][nextx]

        if (gameBoard.inBounds(nextx, nexty) and not gameBoard.isBlank(nextx, nexty) and gameBoard.grid[nexty][nextx].team != self.team) or (type(potPawn).__name__ == "Pawn" and potPawn.team == oppTeam and lastPiece == "Pawn" and potPawn.location == currPos and lastMoveDiff == 2):
            paths.append(chr(nextx + 65) + str(8 - nexty))

        return paths

    def toString(self):
        if(self.team == 'W'):
            #return "\033[94mP  \033[0m"
            return "\u265F  "
        elif(self.team == 'B'):
            #return "\033[93mP  \033[0m"
            return "\u2659  "
