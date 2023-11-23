from src.graphica.IPrimitive import IPrimitive

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
        pass #print(f"Drawing Circle: ({self.x1}, {self.y1}) with radius {self.radius}")
        
    def draw_myself(self):
        pass