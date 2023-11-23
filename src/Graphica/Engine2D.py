from tkinter import Canvas, Tk, CENTER
from graphica.IPrimitive import IPrimitive

class Engine2D:
    width: int
    height: int
    current_color: str
    _canvas: Canvas
    _root: Tk
    _primitives: list[IPrimitive]
    def __init__(self, width:int, height:int):
        self.width = width
        self.height = height
        self._root = Tk()
        self._root.title("Приложение на Tkinter")
        self._root.geometry("640x480") 
        self._primitives = []
        self.current_color = "black"
        self._canvas = Canvas(bg="white", borderwidth=0, width=640, height=480)
        self._canvas.pack(anchor=CENTER, expand=1)

    def set_color(self, color: str):
        self.current_color = color

    def add_shape(self, shape: IPrimitive):
        shape.set_canvas(self._canvas)
        self._primitives.append(shape)

    def draw(self):
        for shape in self._primitives:
            shape.draw(self.current_color)
        self._primitives = []
        self._root.update_idletasks()
        self._root.update()

    def mainloop(self):
        self._root.mainloop()
        