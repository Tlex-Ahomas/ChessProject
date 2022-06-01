import Piece
from Piece import Piece


class Blank(Piece):

    location = ""

    def __init__(self, x, y):
        self.location = x + y

    def move(self):
        print("How did you try to move a blank space bozo")

    def calcPaths(self):
        return []