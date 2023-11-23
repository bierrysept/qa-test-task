from src.graphica.Circle import Circle

class TestCircle:
    def test_circle(self):
        circle = Circle(10,10,5)
        assert circle.x == 10
        assert circle.y == 10
        assert circle.radius == 5

class CircleImitation(Circle):
    pass