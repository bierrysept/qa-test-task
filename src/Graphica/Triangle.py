from graphica.IPrimitive import IPrimitive

class Triangle(IPrimitive):
    x1:int
    y1:int
    x2:int
    y2:int
    x3:int
    y3:int
    def __init__(self, x1:int, y1:int, x2:int, y2:int, x3:int, y3:int):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3

    def print(self):
        print(f"Drawing Triangle: ({self.x1}, {self.y1}) - ({self.x2}, {self.y2}) - ({self.x3}, {self.y3})")
        
    def draw_myself(self, color: str):
        self._canvas.create_polygon(self.x1, self.y1, self.x2, self.y2, self.x3, self.y3, fill="white", outline=color)