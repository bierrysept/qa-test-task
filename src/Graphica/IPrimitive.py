from abc import ABC, abstractmethod
from tkinter import Canvas

class IPrimitive(ABC):

    def set_canvas(self, canvas: Canvas):
        self._canvas = canvas

    def draw(self, color: str):
        self.draw_myself(color)
        self.print()

    @abstractmethod
    def print(self):
        print("Drawing Figure: (Actually this is abstraction)")

    @abstractmethod
    def draw_myself(self, color: str):
        pass