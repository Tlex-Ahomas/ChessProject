from Piece import Piece
from Blank import Blank

class Board:
    grid = 0

    def __init__(self):
        self.grid = [[Blank('A', '1')] * 8] * 8
