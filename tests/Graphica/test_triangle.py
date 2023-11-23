from src.graphica.Triangle import Triangle

class TestTriangle:
    def test_triangle(self):
        triangle = Triangle(10,10,10,20,20,20)
        assert triangle.x1 == 10
        assert triangle.x2 == 10
        assert triangle.x3 == 20
        assert triangle.y1 == 10
        assert triangle.y2 == 20
        assert triangle.y3 == 20