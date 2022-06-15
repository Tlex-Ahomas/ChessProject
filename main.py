# import Piece
import copy
from Board import Board
from CPU import CPU
from Queen import Queen
from Rook import Rook
from Knight import Knight
from Bishop import Bishop


def validInput(p):
    return (len(p) == 2 and 65 <= ord(p[:1]) <= 72 and p[1:].isnumeric() and 1 <= int(p[1:]) <= 8) or p == "castleR" or p == "castleL"


team = 'W'
gameBoard = Board()
bot = False
dacomputer = 0
answer = input("Two player or AI? 2/AI (NOTE: AI is currently experimental) ")
while not(answer == '2' or answer == 'AI'):
    answer = input("Invalid input, options: 2, AI ")

if answer == '2':
    bot = False
elif answer == 'AI':
    bot = True

    botTeam = input("Will CPU be White or Black? W/B ")
    while not(botTeam == 'W' or botTeam == 'B'):
        botTeam = input("Invalid input, options: W, B ")

    botDiff = input("Select CPU difficulty, options: 0, 1, 2 ")
    while not botDiff.isnumeric() and not(int(botDiff) == 0 or int(botDiff) == 1 or int(botDiff) == 2):
        botDiff = input("Invalid input, options: 0, 1, 2 ")

    dacomputer = CPU(botTeam, int(botDiff))

gameBoard.print()

while not(gameBoard.isCheckmate('B') != False or gameBoard.isCheckmate('W') != False):
    if team == 'W':
        alliance = "White"
    elif team == 'B':
        alliance = "Black"

    if bot and dacomputer.team == team:
        cpuMove = dacomputer.makeMove(gameBoard)
        gameBoard.grid = cpuMove[0]
        if cpuMove[1] == "Pawn" and ((team == 'W' and cpuMove[3][1:] == '8') or (team == 'B' and cpuMove[3][1:] == '1')):
            locx = ord(cpuMove[3][:1]) - 65
            locy = 8 - int(cpuMove[3][1:])
            gameBoard.grid[locy][locx] = Queen(locx, locy, team)

        if team == 'W':
            gameBoard.moveListW.append(cpuMove[1] + "-" + cpuMove[2] + " " + cpuMove[3])
            print(gameBoard.moveListW[len(gameBoard.moveListW) - 1])
        else:
            gameBoard.moveListB.append(cpuMove[1] + "-" + cpuMove[2] + " " + cpuMove[3])
            print(gameBoard.moveListB[len(gameBoard.moveListB) - 1])

        if team == 'W':
            team = 'B'
        else:
            team = 'W'
        gameBoard.print()
        continue

    attempt = input(alliance + ": select which piece to move ")
    if not validInput(attempt):
        print("Invalid input")
        continue

    if len(attempt) > 2:
        for r in gameBoard.grid:
            for c in r:
                if type(c).__name__ == "King" and c.team == team:  #finds King
                    tempBoard = copy.deepcopy(gameBoard)  #copies current board to tempBoard
                    if attempt == "castleL":
                        if c.castle('L', tempBoard):  #determines if board was able to castle left
                            gameBoard = copy.deepcopy(tempBoard)
                            if team == 'W':
                                gameBoard.moveListW.append("castle_left")
                                team = 'B'
                            else:
                                gameBoard.moveListB.append("castle_left")
                                team = 'W'
                            break  #for a successful castle, the gameBoard is updated, it becomes the other player's turn, and the rest of the code in the loop is skipped
                        else:
                            print("Conditions for castling left not met")
                            break  #for a failed castle, the gameBoard remains unchanged, it does NOT become the other player's turn, and the rest of the loop is skipped
                    elif attempt == "castleR":  #same as above code but for castling right
                        if c.castle('R', tempBoard):
                            gameBoard = copy.deepcopy(tempBoard)
                            if team == 'W':
                                gameBoard.moveListW.append("castle_right")
                                team = 'B'
                            else:
                                gameBoard.moveListB.append("castle_right")
                                team = 'W'
                            break
                        else:
                            print("Conditions for castling right not met")
                            break
        gameBoard.print()
        continue


    coords = [ord(attempt[:1]) - 65, 8 - int(attempt[1:])]

    if gameBoard.grid[coords[1]][coords[0]].team != team:
        print("You do not have a piece on this space")
        continue
    elif len(gameBoard.grid[coords[1]][coords[0]].calcPaths(gameBoard)) < 1:
        print("This piece cannot be moved")
        continue

    print(gameBoard.grid[coords[1]][coords[0]].calcPaths(gameBoard))
    mv = input("Where would you like to move your " + type(gameBoard.grid[coords[1]][coords[0]]).__name__ + " ")
    if mv == "cancel":
        continue

    movingPiece = type(gameBoard.grid[coords[1]][coords[0]]).__name__
    canceler = False
    while not validInput(mv):
        mv = input("Invalid input, please enter a valid space on the board ")
        if mv == "cancel":
            canceler = True
            break

    if canceler:
        continue

    tempBoard = copy.deepcopy(gameBoard)
    while not tempBoard.grid[coords[1]][coords[0]].move(mv[:1], mv[1:], tempBoard) or tempBoard.isCheck(team):
        tempBoard = copy.deepcopy(gameBoard)
        mv = input("That piece cannot move there, please select a valid position to move it to ")
        if mv == "cancel":
            canceler = True
            break

    if canceler:
        continue

    if type(tempBoard.grid[8 - int(mv[1:])][ord(mv[:1]) - 65]).__name__ == "Pawn" and ((mv[1:] == '8' and team == 'W') or (mv[1:] == '1' and team == 'B')):
        tempBoard.print()
        ans = input("You can promote your pawn, options: Q for Queen, R for Rook, B for Bishop, K for Knight ")
        while not (ans == "Q" or ans == "R" or ans == "B" or ans == "K"):
            ans = input("Invalid input, options: Q for Queen, R for Rook, B for Bishop, K for Knight ")
        if ans == "Q":
            gameBoard[8 - int(mv[1:])][ord(mv[:1]) - 65] = Queen(mv[:1], mv[1:], team)
        elif ans == "R":
            gameBoard[8 - int(mv[1:])][ord(mv[:1]) - 65] = Rook(mv[:1], mv[1:], team)
        elif ans == "B":
            gameBoard[8 - int(mv[1:])][ord(mv[:1]) - 65] = Bishop(mv[:1], mv[1:], team)
        elif ans == "K":
            gameBoard[8 - int(mv[1:])][ord(mv[:1]) - 65] = Knight(mv[:1], mv[1:], team)

    gameBoard = copy.deepcopy(tempBoard)

    if team == 'W':
        gameBoard.moveListW.append(movingPiece + "-" + attempt + " " + mv)
    else:
        gameBoard.moveListB.append(movingPiece + "-" + attempt + " " + mv)

    gameBoard.print()
    if team == 'W':
        team = 'B'
    else:
        team = 'W'


if (gameBoard.isCheckmate('B')):
    print("White Wins!")
else:
    print("Black Wins")

# eventually we put the driver code here

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
