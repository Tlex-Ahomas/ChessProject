from abc import ABC, abstractmethod

class Piece(ABC):

    @property
    def location(self):
        pass

    @property
    def team(self):
        pass

    @abstractmethod
    def move(self, x, y, b):
        pass

    @abstractmethod
    def calcPaths(self, b):
        pass

    @abstractmethod
    def toString(self):
        pass
