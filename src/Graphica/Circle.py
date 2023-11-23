from graphica.IPrimitive import IPrimitive

class Circle(IPrimitive):
    x: int
    y: int
    radius: int

    def __init__(self, x:int, y:int, radius:int):
        self.x = x
        self.y = y
        self.radius = radius

    def print(self):
        print(f"Drawing Circle: ({self.x}, {self.y}) with radius {self.radius}")
        
    def draw_myself(self, color: str):
        self._canvas.create_oval(self.x-self.radius, self.y-self.radius, self.x+self.radius, self.y+self.radius, fill="white", outline=color)