from typing import Union
from src.graphica.Circle import Circle
from tkinter import Canvas

class TestCircle:
    def test_circle(self):
        circle = CircleImitation(10,10,5)
        assert circle.x == 10
        assert circle.y == 10
        assert circle.radius == 5
    
    def test_set_canvas(self):
        circle = CircleImitation(10,10,5)
        canvas = Canvas()
        circle.set_canvas(canvas)
        assert circle.canvas_is(canvas)

class CircleImitation(Circle):
    def canvas_is(self, canvas: Union [Canvas, None]):
        return self._canvas == canvas