from Piece import Piece


class Pawn(Piece):

    location = ""

    def __init__(self, x, y):
        self.location = x + y

    def move(self):
        return

    def calcPaths(self):
        return