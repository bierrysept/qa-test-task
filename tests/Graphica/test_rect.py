from src.graphica.Rect import Rect

class TestRect:
    def test_create_rect(self):
        rect = Rect(10, 10, 20, 20)
        assert rect.x == 10
        assert rect.y == 10
        assert rect.width == 20
        assert rect.height == 20