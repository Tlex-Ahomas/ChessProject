from abc import ABC, abstractmethod

class Piece(ABC):

    @property
    def location(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def calcPaths(self):
        pass