# import Piece
import GameBoard
from Board import Board


def validInput(p):
    return (len(p) == 2 and 65 <= ord(p[:1]) <= 72 and p[1:].isnumeric() and 1 <= int(p[1:]) <= 8) or p == "castleR" or p == "castleL"


team = 'W'
gameBoard = Board()
gameBoard.print()

while not(gameBoard.isCheckmate('B') != False or gameBoard.isCheckmate('W') != False):
    attempt = input(team + ": select which piece to move ")
    if not validInput(attempt):
        print("Invalid input")
        continue

    if len(attempt) > 2:
        for r in gameBoard.grid:
            for c in r:
                if type(c).__name__ == "King" and c.team == team:  #finds King
                    tempBoard = gameBoard  #copies current board to tempBoard
                    if attempt == "castleL":
                        if c.castle('L', tempBoard):  #determines if board was able to castle left
                            gameBoard = tempBoard
                            if team == 'W':
                                team = 'B'
                            else:
                                team = 'W'
                            break  #for a successful castle, the gameBoard is updated, it becomes the other player's turn, and the rest of the code in the loop is skipped
                        else:
                            print("Conditions for castling left not met")
                            break  #for a failed castle, the gameBoard remains unchanged, it does NOT become the other player's turn, and the rest of the loop is skipped
                    elif attempt == "castleR":  #same as above code but for castling right
                        if c.castle('R', tempBoard):
                            gameBoard = tempBoard
                            if team == 'W':
                                team = 'B'
                            else:
                                team = 'W'
                            break
                        else:
                            print("Conditions for castling right not met")
                            break
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

    while not validInput(mv):
        mv = input("Invalid input, please enter a valid space on the board ")

    tempBoard = gameBoard

    while not tempBoard.grid[coords[1]][coords[0]].move(mv[:1], mv[1:], tempBoard) and not tempBoard.isCheck(team):
        tempBoard = gameBoard
        mv = input("That piece cannot move there, please select a valid position to move it to ")
    gameBoard = tempBoard
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
