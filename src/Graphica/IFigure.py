from abc import ABC, abstractmethod

class IFigure(ABC):

    def draw(self):
        self.print("Drawing Figure: (Actually this is abstraction)")

    @abstractmethod
    def print(self, text: str):
        pass