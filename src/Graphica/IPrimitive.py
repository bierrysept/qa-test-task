from abc import ABC, abstractmethod

class IPrimitive(ABC):

    def draw(self):
        self.draw_myself()
        self.print()

    @abstractmethod
    def print(self):
        print("Drawing Figure: (Actually this is abstraction)")

    @abstractmethod
    def draw_myself(self):
        pass