# import Piece
import GameBoard
from Board import Board


gameBoard = Board()
GameBoard.gb = gameBoard
gameBoard.print()
print()
print(gameBoard.grid[6][0].move('B', '3'))
gameBoard.print()
# eventually we put the driver code here

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
