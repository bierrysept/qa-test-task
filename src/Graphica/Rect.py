from graphica.IPrimitive import IPrimitive

class Rect(IPrimitive): 
    x:int 
    y:int 
    width:int
    height:int 

    def __init__(self, x:int, y:int, width:int, height:int):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def print(self):
        print(f"Drawing Rectangle: ({self.x}, {self.y}) with width {self.width} and height {self.height}")
        
    def draw_myself(self, color: str):
        self._canvas.create_rectangle(self.x, self.y, self.x+self.width, self.y+self.height, fill="white", outline=color)