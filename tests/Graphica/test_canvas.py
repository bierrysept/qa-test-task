from src.graphica.Canvas import Canvas

class TestCanvas:
    def test_init(self):
        canvas1 = Canvas(1,2)
        assert canvas1.width == 1
        assert canvas1.height == 2