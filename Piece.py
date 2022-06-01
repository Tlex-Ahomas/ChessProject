from abc import ABC, abstractmethod

class Piece(ABC):

    @property
    def location(self):
        pass

    @property
    def team(self):
        pass

    @abstractmethod
    def move(self, x, y):
        pass

    @abstractmethod
    def calcPaths(self):
        pass

    @abstractmethod
    def toString(self):
        pass
