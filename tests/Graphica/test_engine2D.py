from src.graphica.Engine2D import Engine2D
from graphica.Triangle import Triangle
from graphica.Circle import Circle

class TestEngine2D:
    def test_create_engine2D(self):
        engine = Engine2D(100, 100)
        assert engine.width == 100
        assert engine.height == 100
        assert engine.current_color == "black"

    def test_set_color(self):
        engine = Engine2D(100, 100)
        engine.set_color("red")
        assert engine.current_color == "red"

    def test_engine_draw(self):
        engine = ImitateEngine2D(100, 100)
        circle = Circle(10, 10, 5)
        engine.add_shape(circle)
        engine.set_color("red")
        triangle = Triangle(20, 10, 25, 0, 30, 10)
        engine.add_shape(triangle)
        engine.draw()
        assert engine.premitives_is_empty()  # Проверяем, что после отрисовки список фигур на холсте пуст

class ImitateEngine2D(Engine2D):
    def premitives_is_empty(self):
        return len(self._primitives) == 0