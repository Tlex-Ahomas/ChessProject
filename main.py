# import Piece
import GameBoard
from Board import Board


def validInput(p):
    return len(p) == 2 and 65 <= ord(p[:1]) <= 72 and p[1:].isnumeric() and 1 <= int(p[1:]) <= 8


team = 'W'
gameBoard = Board()
gameBoard.print()

while True:
    attempt = input(team + ": select which piece to move ")
    if not validInput(attempt):
        print("Invalid input")
        continue

    coords = [ord(attempt[:1]) - 65, 8 - int(attempt[1:])]

    if gameBoard.grid[coords[1]][coords[0]].team != team:
        print("You do not have a piece on this space")
        continue
    elif len(gameBoard.grid[coords[1]][coords[0]].calcPaths(gameBoard)) < 1:
        print("This piece cannot be moved")
        print(gameBoard.grid[coords[1]][coords[0]].calcPaths(gameBoard))
        continue

    print(gameBoard.grid[coords[1]][coords[0]].calcPaths(gameBoard))
    mv = input("Where would you like to move your " + type(gameBoard.grid[coords[1]][coords[0]]).__name__ + " ")

    while not validInput(mv):
        mv = input("Invalid input, please enter a valid space on the board ")

    while not gameBoard.grid[coords[1]][coords[0]].move(mv[:1], mv[1:], gameBoard):
        mv = input("That piece cannot move there, please select a valid position to move it to ")
    gameBoard.print()
    if team == 'W':
        team = 'B'
    else:
        team = 'W'




# eventually we put the driver code here

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
