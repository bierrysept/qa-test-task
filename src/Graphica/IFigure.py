from abc import ABC, abstractmethod

class Figure(ABC):

    def draw(self):
        self.print("Drawing Figure: (Actually this is abstraction)")

    @abstractmethod
    def print(self, text: str):
        pass