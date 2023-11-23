from src.graphica.IPrimitive import IPrimitive

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
        
    def draw_myself(self):
        pass