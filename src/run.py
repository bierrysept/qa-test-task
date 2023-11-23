import time

from graphica.Engine2D import Engine2D
from graphica.Triangle import Triangle
from graphica.Rect import Rect
from graphica.Circle import Circle

engine = Engine2D(640, 480)
time.sleep(1)

triangle = Triangle(20, 170, 170, 20, 320, 170)
engine.add_shape(triangle)
engine.draw()
time.sleep(1)

rect = Rect(100, 100, 100, 100)
engine.add_shape(rect)

circle = Circle(50, 50, 50)
engine.add_shape(circle)
engine.draw()
time.sleep(1)
engine.mainloop()
